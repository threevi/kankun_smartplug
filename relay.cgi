#!/usr/bin/env lua

RELAY_PATH = "/sys/class/leds/tp-link:blue:relay/brightness"
QUERY_STRING = os.getenv("QUERY_STRING")
RELAY_CTRL = io.open(RELAY_PATH, "r+")

function status()
	RELAY_CTRL:seek("set")
	if RELAY_CTRL:read() == "0" then
		print("{\"power\": \"off\"}")
	else
		print("{\"power\": \"on\"}")
	end
end

print([[
Content-Type: text/plain
Cache-Control: no-cache, must-revalidate
]])

if QUERY_STRING == "on" then
	RELAY_CTRL:write("1")
	status()
elseif QUERY_STRING == "off" then
	RELAY_CTRL:write("0")
	status()
elseif QUERY_STRING == "toggle" then
	if RELAY_CTRL:read() == "0" then
		RELAY_CTRL:write("1")
	else
		RELAY_CTRL:write("0")
	end
	status()
elseif QUERY_STRING == "status" then
	status()
else
	print("{\"error\": \"Unknown argument\"}")
end

RELAY_CTRL:close()
