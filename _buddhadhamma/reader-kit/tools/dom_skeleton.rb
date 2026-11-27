# 输出 kramdown HTML 的标签骨架（标签名+属性，不含文字），用于比对结构是否变化
require 'kramdown'
t=STDIN.read.sub(/\A---\n.*?\n---\n/m,'')
puts Kramdown::Document.new(t).to_html.scan(/<[^>]+>/).join("\n")
