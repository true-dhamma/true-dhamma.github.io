---
title: 佛法 Buddhadhamma 中文版
permalink: "/buddhadhamma/"
layout: doc
feature_text: 
feature_image: "/uploads/top_banner_dhamma.jpg"
excerpt: 
---

# 佛法 Buddhadhamma 中文版

<ul>
  {% for item in site.buddhadhamma %}
    <li>
      <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
      <!-- 你还可以显示其他信息，例如日期 -->
      <!-- <span> - {{ item.date | date: "%Y-%m-%d" }}</span> -->
    </li>
  {% endfor %}
</ul>