#!/usr/bin/crystal

require "http/server"
require "mime" # helps determine correct Content-Type

PUBLIC_DIR = "./public" # Place index.html in this folder

server = HTTP::Server.new do |context|
path = context.request.path
filepath = File.join(PUBLIC_DIR, path == "/" ? "index.html" : path)

if File.exists?(filepath)
# Get correct Content-Type based on extension
  context.response.content_type = MIME.from_filename(filepath)
context.response.print File.read(filepath)
  else
  context.response.status_code = 404
  context.response.content_type = "text/plain"
  context.response.print "404 Not Found: #{path}"
  end
  end

  address = server.bind_tcp 8080
  puts "Serving files on http://#{address}"
  server.listen

