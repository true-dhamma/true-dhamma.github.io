#!/usr/bin/env ruby
# Read-only full-book kramdown parse. Usage: ruby check-kramdown.rb [repo-root]
require 'kramdown'
require 'json'
root = ARGV[0] || '/workspace/bd-thai-all'
files = Dir[File.join(root, '_buddhadhamma', '*.md')].sort
abort 'No book Markdown files found' if files.empty?
result = {ruby: RUBY_VERSION, kramdown: Kramdown::VERSION, files: files.size, warnings: [], footnote_references: 0, footnote_definitions: 0}
files.each do |file|
  text = File.read(file, encoding: 'utf-8').sub(/\A---\n.*?\n---\n/m, '')
  doc = Kramdown::Document.new(text)
  html = doc.to_html
  doc.warnings.each { |w| result[:warnings] << {file: File.basename(file), warning: w} }
  result[:footnote_references] += html.scan(/id="fr-fn\d+"/).size
  result[:footnote_definitions] += html.scan(/id="fn-fn\d+"/).size
end
result[:warning_count] = result[:warnings].size
puts JSON.pretty_generate(result)
exit(result[:warning_count].zero? && result[:footnote_references] == 2120 && result[:footnote_definitions] == 2120 ? 0 : 1)
