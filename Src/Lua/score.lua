require 'nes_interface'

function get_score()
  local p1score = memory.readbyte(0x07E3)
  local p2score = memory.readbyte(0x07E5)
  return p1score
end

x_position_last = 0

--get_position  x
function get_position()
    local x_position = memory.readbyte(0x0334)
    local temp = x_position - x_position_last
    x_position_last = x_position
    return temp
end

-- get x_position_reward
function get_x_reward()
    local _reward = get_position()
    if _reward < -5 or _reward > 5 then
        return 0
    end
    return _reward
end

-- death penalty sub 30
function get_penalty()
    if memory.readbyte(0x0090) == 00 then
        return -30
    end
    return 0
end

count = 0
time_first = os.clock()

function _time_penalty()
    if count == 3 then
        local time_end = os.clock()
        local reward = time_end - time_first
        time_first = time_end
        count = 0
        return reward
    else
        count = count + 1
        return 0
    end
end

function get_reward()
    return _time_penalty() + get_penalty() + get_x_reward()
end

nes_init()

local score = 0

while true do
  -- update screen every screen_update_interval frames
  local frame_skip = 4

  if emu.framecount() % frame_skip == 0 then
    nes_ask_for_command()
    local has_command = nes_process_command()
    if has_command then
      emu.frameadvance()
      local reward = 0
      if nes_get_reset_flag() then
        nes_clear_reset_flag()
        score = 0
        reward = 0
      else
        local new_score = get_score()
        --  take reward by time x_position and is death
        reward = get_reward()
        score = new_score
      end
      nes_send_data(string.format("%02x%02x", reward, score))
      nes_update_screen()
    else
      print('pipe closed')
      break
    end
  else
    -- skip frames
    emu.frameadvance()
  end
end
