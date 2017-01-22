#!/usr/bin/env lua

RELAY_PATH = "/sys/class/leds/tp-link:blue:relay/brightness"
QUERY_STRING = os.getenv("QUERY_STRING")
RELAY_CTRL = io.open(RELAY_PATH, "r+")

print([[
Content-Type: text/plain
Cache-Control: no-cache, must-revalidate
]])

if QUERY_STRING == "on" then
	RELAY_CTRL:write("1")
	print("OK")
elseif QUERY_STRING == "off" then
	RELAY_CTRL:write("0")
	print("OK")
elseif QUERY_STRING == "status" then
	print(RELAY_CTRL:read())
else
	print("FAILURE")
end

RELAY_CTRL:close()
