source "https://rubygems.org"

# 从 .gemspec 文件加载主题的默认依赖
gemspec

# ----------------------------------------------------
# 最终解决方案：
# 将 jekyll-sass-converter 降级到 2.x 版本。
# 这个版本系列依赖的是旧的、更稳定的 sassc 库，
# 从而完全绕开 sass-embedded 的安装问题。
gem "jekyll-sass-converter", "~> 2.2.0"
# ----------------------------------------------------