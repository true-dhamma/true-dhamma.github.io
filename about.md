---
title: 关于
feature_text: |
  A demo of Markdown and HTML includes
feature_image: https://picsum.photos/2560/600?image=873
excerpt: A demo of Markdown and HTML includes
aside: true
---
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

<small>A small element</small>

[A link](https://david.darn.es "A link")

Lorem ipsum dolor sit amet, consectetur adip\* isicing elit, sed do eiusmod \*tempor incididunt ut labore et dolore magna aliqua.

Duis aute irure dolor in [A link](https://david.darn.es "A link") reprehenderit in voluptate velit esse cillum **bold text** dolore eu fugiat nulla pariatur. Excepteur span element sint occaecat cupidatat non proident, sunt *italicised text* in culpa qui officia deserunt mollit anim id `some code` est laborum.

* An item
* An item
* An item
* An item
* An item

1. Item one
2. Item two
3. Item three
4. Item four
5. Item five

> A simple blockquote

Some HTML…

\`\`\` html

> You planning a vacation, Mr. Sullivan?
>
> <footer>
>     <a href="http://www.imdb.com/title/tt0284978/quotes/qt1375101">Sunways Security Guard</a>
>   </footer>
{: cite="http://www.imdb.com/title/tt0284978/quotes/qt1375101"}

\`\`\`

…CSS…

`css blockquote {   text-align: center;   font-weight: bold; } blockquote footer {   font-size: .8rem; } `

…and JavaScript

\`\`\` js const blockquote = document.querySelector(“blockquote”) const bolden = (keyString, string) =&gt;   string.replace(new RegExp(keyString, ‘g’), ‘**‘+keyString+’**’)

blockquote.innerHTML = bolden(“Mr. Sullivan”, blockquote.innerHTML) \`\`\`

`Single line of code`

## HTML Includes

### Contact form

{% include site-form.html %}

`html <span data-cms-snippet-type="inline" data-cms-snippet-id="fa403fb8-d4c1-44fc-b4f7-a18d3df61c24" data-cms-snippet-data="eyJ0cmltX3RvcF9sZWZ0IjpmYWxzZSwidHJpbV90b3BfcmlnaHQiOmZhbHNlLCJjb250ZW50IjoieyUgaW5jbHVkZSBzaXRlLWZvcm0uaHRtbCAlfSIsInRyaW1fYm90dG9tX2xlZnQiOmZhbHNlLCJ0cmltX2JvdHRvbV9yaWdodCI6ZmFsc2UsIl9zbmlwcGV0X3R5cGUiOiJqZWt5bGxfcmF3IiwiX21ldGEiOnsidHJpbV90b3BfbGVmdCI6e30sInRyaW1fdG9wX3JpZ2h0Ijp7fSwiY29udGVudCI6eyJvcmlnaW5hbERhdGEiOlt7Il90eXBlIjoidGV4dCIsInRleHQiOiJ7JSBpbmNsdWRlIHNpdGUtZm9ybS5odG1sICV9In1dfSwidHJpbV9ib3R0b21fbGVmdCI6e30sInRyaW1fYm90dG9tX3JpZ2h0Ijp7fX19"></span> `

### Demo map embed

{% include map.html id="1UT-2Z-Vg_MG_TrS5X2p8SthsJhc" title="Coffee shop map" %}

`html <span data-cms-snippet-type="inline" data-cms-snippet-id="26af6913-3281-4304-ab4e-3500d23b1ade" data-cms-snippet-data="eyJ0cmltX3RvcF9sZWZ0IjpmYWxzZSwidHJpbV90b3BfcmlnaHQiOmZhbHNlLCJjb250ZW50IjoieyUgaW5jbHVkZSBtYXAuaHRtbCBpZD1cIlhYWFhYWFwiIHRpdGxlPVwiQ29mZmVlIHNob3AgbWFwXCIgJX0iLCJ0cmltX2JvdHRvbV9sZWZ0IjpmYWxzZSwidHJpbV9ib3R0b21fcmlnaHQiOmZhbHNlLCJfc25pcHBldF90eXBlIjoiamVreWxsX3JhdyIsIl9tZXRhIjp7InRyaW1fdG9wX2xlZnQiOnt9LCJ0cmltX3RvcF9yaWdodCI6e30sImNvbnRlbnQiOnsib3JpZ2luYWxEYXRhIjpbeyJfdHlwZSI6InRleHQiLCJ0ZXh0IjoieyUgaW5jbHVkZSBtYXAuaHRtbCBpZD1cIlhYWFhYWFwiIHRpdGxlPVwiQ29mZmVlIHNob3AgbWFwXCIgJX0ifV19LCJ0cmltX2JvdHRvbV9sZWZ0Ijp7fSwidHJpbV9ib3R0b21fcmlnaHQiOnt9fX0="></span> `

### Button include

{% include button.html text="A button" link="https://david.darn.es" %}

{% include button.html text="A button with icon" link="https://twitter.com/daviddarnes" icon="twitter" %}

`html <span data-cms-snippet-type="inline" data-cms-snippet-id="2cffe8f8-979f-4968-a0e7-030cd4c4dfb4" data-cms-snippet-data="eyJ0cmltX3RvcF9sZWZ0IjpmYWxzZSwidHJpbV90b3BfcmlnaHQiOmZhbHNlLCJjb250ZW50IjoieyUgaW5jbHVkZSBidXR0b24uaHRtbCB0ZXh0PVwiQSBidXR0b25cIiBsaW5rPVwiaHR0cHM6Ly9kYXZpZC5kYXJuLmVzXCIgJX1cbnslIGluY2x1ZGUgYnV0dG9uLmh0bWwgdGV4dD1cIkEgYnV0dG9uIHdpdGggaWNvblwiIGxpbms9XCJodHRwczovL3R3aXR0ZXIuY29tL2RhdmlkZGFybmVzXCIgaWNvbj1cInR3aXR0ZXJcIiAlfSIsInRyaW1fYm90dG9tX2xlZnQiOmZhbHNlLCJ0cmltX2JvdHRvbV9yaWdodCI6ZmFsc2UsIl9zbmlwcGV0X3R5cGUiOiJqZWt5bGxfcmF3IiwiX21ldGEiOnsidHJpbV90b3BfbGVmdCI6e30sInRyaW1fdG9wX3JpZ2h0Ijp7fSwiY29udGVudCI6eyJvcmlnaW5hbERhdGEiOlt7Il90eXBlIjoidGV4dCIsInRleHQiOiJ7JSBpbmNsdWRlIGJ1dHRvbi5odG1sIHRleHQ9XCJBIGJ1dHRvblwiIGxpbms9XCJodHRwczovL2RhdmlkLmRhcm4uZXNcIiAlfVxueyUgaW5jbHVkZSBidXR0b24uaHRtbCB0ZXh0PVwiQSBidXR0b24gd2l0aCBpY29uXCIgbGluaz1cImh0dHBzOi8vdHdpdHRlci5jb20vZGF2aWRkYXJuZXNcIiBpY29uPVwidHdpdHRlclwiICV9In1dfSwidHJpbV9ib3R0b21fbGVmdCI6e30sInRyaW1fYm90dG9tX3JpZ2h0Ijp7fX19"></span> `

### Icon include

{% include icon.html id="twitter" title="twitter" %} [{% include icon.html id="linkedin" title="twitter" %}](https://www.linkedin.com/in/daviddarnes)

`html <span data-cms-snippet-type="inline" data-cms-snippet-id="e88dc872-d94f-40f5-8b52-dcefebb12227" data-cms-snippet-data="eyJ0cmltX3RvcF9sZWZ0IjpmYWxzZSwidHJpbV90b3BfcmlnaHQiOmZhbHNlLCJjb250ZW50IjoieyUgaW5jbHVkZSBpY29uLmh0bWwgaWQ9XCJ0d2l0dGVyXCIgdGl0bGU9XCJ0d2l0dGVyXCIgJX1cblt7JSBpbmNsdWRlIGljb24uaHRtbCBpZD1cImxpbmtlZGluXCIgdGl0bGU9XCJ0d2l0dGVyXCIgJX1dKGh0dHBzOi8vd3d3LmxpbmtlZGluLmNvbS9pbi9kYXZpZGRhcm5lcykiLCJ0cmltX2JvdHRvbV9sZWZ0IjpmYWxzZSwidHJpbV9ib3R0b21fcmlnaHQiOmZhbHNlLCJfc25pcHBldF90eXBlIjoiamVreWxsX3JhdyIsIl9tZXRhIjp7InRyaW1fdG9wX2xlZnQiOnt9LCJ0cmltX3RvcF9yaWdodCI6e30sImNvbnRlbnQiOnsib3JpZ2luYWxEYXRhIjpbeyJfdHlwZSI6InRleHQiLCJ0ZXh0IjoieyUgaW5jbHVkZSBpY29uLmh0bWwgaWQ9XCJ0d2l0dGVyXCIgdGl0bGU9XCJ0d2l0dGVyXCIgJX1cblt7JSBpbmNsdWRlIGljb24uaHRtbCBpZD1cImxpbmtlZGluXCIgdGl0bGU9XCJ0d2l0dGVyXCIgJX1dKGh0dHBzOi8vd3d3LmxpbmtlZGluLmNvbS9pbi9kYXZpZGRhcm5lcykifV19LCJ0cmltX2JvdHRvbV9sZWZ0Ijp7fSwidHJpbV9ib3R0b21fcmlnaHQiOnt9fX0="></span> `

### Video include

{% include video.html id="zrkcGL5H3MU" title="Siteleaf tutorial video" %}

`html <span data-cms-snippet-type="inline" data-cms-snippet-id="ee33a7c6-cd95-486b-99ec-17ad500af60b" data-cms-snippet-data="eyJ0cmltX3RvcF9sZWZ0IjpmYWxzZSwidHJpbV90b3BfcmlnaHQiOmZhbHNlLCJjb250ZW50IjoieyUgaW5jbHVkZSB2aWRlby5odG1sIGlkPVwienJrY0dMNUgzTVVcIiB0aXRsZT1cIlNpdGVsZWFmIHR1dG9yaWFsIHZpZGVvXCIgJX0iLCJ0cmltX2JvdHRvbV9sZWZ0IjpmYWxzZSwidHJpbV9ib3R0b21fcmlnaHQiOmZhbHNlLCJfc25pcHBldF90eXBlIjoiamVreWxsX3JhdyIsIl9tZXRhIjp7InRyaW1fdG9wX2xlZnQiOnt9LCJ0cmltX3RvcF9yaWdodCI6e30sImNvbnRlbnQiOnsib3JpZ2luYWxEYXRhIjpbeyJfdHlwZSI6InRleHQiLCJ0ZXh0IjoieyUgaW5jbHVkZSB2aWRlby5odG1sIGlkPVwienJrY0dMNUgzTVVcIiB0aXRsZT1cIlNpdGVsZWFmIHR1dG9yaWFsIHZpZGVvXCIgJX0ifV19LCJ0cmltX2JvdHRvbV9sZWZ0Ijp7fSwidHJpbV9ib3R0b21fcmlnaHQiOnt9fX0="></span> `

### Image includes

{% include figure.html image="https://picsum.photos/600/800?image=894" caption="Image with caption" width="300" height="800" %}

{% include figure.html image="https://picsum.photos/600/800?image=894" caption="Right aligned image" position="right" width="300" height="800" %}

{% include figure.html image="https://picsum.photos/600/800?image=894" caption="Left aligned image" position="left" width="300" height="800" %}

{% include figure.html image="https://picsum.photos/1600/800?image=894" alt="Image with just alt text" %}

`html <span data-cms-snippet-type="inline" data-cms-snippet-id="54704393-f5b4-4931-9db2-27d9bacb775f" data-cms-snippet-data="eyJ0cmltX3RvcF9sZWZ0IjpmYWxzZSwidHJpbV90b3BfcmlnaHQiOmZhbHNlLCJjb250ZW50IjoieyUgaW5jbHVkZSBmaWd1cmUuaHRtbCBpbWFnZT1cImh0dHBzOi8vcGljc3VtLnBob3Rvcy82MDAvODAwP2ltYWdlPTg5NFwiIGNhcHRpb249XCJJbWFnZSB3aXRoIGNhcHRpb25cIiB3aWR0aD1cIjMwMFwiIGhlaWdodD1cIjgwMFwiICV9XG5cbnslIGluY2x1ZGUgZmlndXJlLmh0bWwgaW1hZ2U9XCJodHRwczovL3BpY3N1bS5waG90b3MvNjAwLzgwMD9pbWFnZT04OTRcIiBjYXB0aW9uPVwiUmlnaHQgYWxpZ25lZCBpbWFnZVwiIHBvc2l0aW9uPVwicmlnaHRcIiB3aWR0aD1cIjMwMFwiIGhlaWdodD1cIjgwMFwiICV9XG5cbnslIGluY2x1ZGUgZmlndXJlLmh0bWwgaW1hZ2U9XCJodHRwczovL3BpY3N1bS5waG90b3MvNjAwLzgwMD9pbWFnZT04OTRcIiBjYXB0aW9uPVwiTGVmdCBhbGlnbmVkIGltYWdlXCIgcG9zaXRpb249XCJsZWZ0XCIgd2lkdGg9XCIzMDBcIiBoZWlnaHQ9XCI4MDBcIiAlfVxuXG57JSBpbmNsdWRlIGZpZ3VyZS5odG1sIGltYWdlPVwiaHR0cHM6Ly9waWNzdW0ucGhvdG9zLzE2MDAvODAwP2ltYWdlPTg5NFwiIGFsdD1cIkltYWdlIHdpdGgganVzdCBhbHQgdGV4dFwiICV9IiwidHJpbV9ib3R0b21fbGVmdCI6ZmFsc2UsInRyaW1fYm90dG9tX3JpZ2h0IjpmYWxzZSwiX3NuaXBwZXRfdHlwZSI6Impla3lsbF9yYXciLCJfbWV0YSI6eyJ0cmltX3RvcF9sZWZ0Ijp7fSwidHJpbV90b3BfcmlnaHQiOnt9LCJjb250ZW50Ijp7Im9yaWdpbmFsRGF0YSI6W3siX3R5cGUiOiJ0ZXh0IiwidGV4dCI6InslIGluY2x1ZGUgZmlndXJlLmh0bWwgaW1hZ2U9XCJodHRwczovL3BpY3N1bS5waG90b3MvNjAwLzgwMD9pbWFnZT04OTRcIiBjYXB0aW9uPVwiSW1hZ2Ugd2l0aCBjYXB0aW9uXCIgd2lkdGg9XCIzMDBcIiBoZWlnaHQ9XCI4MDBcIiAlfVxuXG57JSBpbmNsdWRlIGZpZ3VyZS5odG1sIGltYWdlPVwiaHR0cHM6Ly9waWNzdW0ucGhvdG9zLzYwMC84MDA/aW1hZ2U9ODk0XCIgY2FwdGlvbj1cIlJpZ2h0IGFsaWduZWQgaW1hZ2VcIiBwb3NpdGlvbj1cInJpZ2h0XCIgd2lkdGg9XCIzMDBcIiBoZWlnaHQ9XCI4MDBcIiAlfVxuXG57JSBpbmNsdWRlIGZpZ3VyZS5odG1sIGltYWdlPVwiaHR0cHM6Ly9waWNzdW0ucGhvdG9zLzYwMC84MDA/aW1hZ2U9ODk0XCIgY2FwdGlvbj1cIkxlZnQgYWxpZ25lZCBpbWFnZVwiIHBvc2l0aW9uPVwibGVmdFwiIHdpZHRoPVwiMzAwXCIgaGVpZ2h0PVwiODAwXCIgJX1cblxueyUgaW5jbHVkZSBmaWd1cmUuaHRtbCBpbWFnZT1cImh0dHBzOi8vcGljc3VtLnBob3Rvcy8xNjAwLzgwMD9pbWFnZT04OTRcIiBhbHQ9XCJJbWFnZSB3aXRoIGp1c3QgYWx0IHRleHRcIiAlfSJ9XX0sInRyaW1fYm90dG9tX2xlZnQiOnt9LCJ0cmltX2JvdHRvbV9yaWdodCI6e319fQ=="></span> `