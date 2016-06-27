notebook = pistes-cyclables

all:
	ipython nbconvert $(notebook).ipynb --to slides
	#sed -i 's:<link rel="stylesheet" href="//cdn.jsdelivr.net/reveal.js/2.4.0/css/theme/simple.css" id="theme">:<link rel="stylesheet" href="classy.css" id="theme">:' $(notebook).slides.html $<
	#Modified @media print to not override all the pygment coloring with black
	sed -i 's:@media print{*{text-shadow:none !important;color:#000 !important;background:transparent !important;box-shadow:none !important;} a,a:visited{text-decoration:underline;} a[href]:after{content:" (" attr(href) ")";} abbr[title]:after{content:" (" attr(title) ")";} .ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:"";} pre,blockquote{border:1px solid #999;page-break-inside:avoid;} thead{display:table-header-group;} tr,img{page-break-inside:avoid;} img{max-width:100% !important;} @page {margin:0.5cm;}p,h2,h3{orphans:3;widows:3;} h2,h3{page-break-after:avoid;}}body{margin:0;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:13px;line-height:20px;color:#000000;background-color:#ffffff;}:@media print{*{text-shadow:none !important;background:transparent !important;box-shadow:none !important;} a,a:visited{text-decoration:underline;} a[href]:after{content:" (" attr(href) ")";} abbr[title]:after{content:" (" attr(title) ")";} .ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:"";} pre,blockquote{border:1px solid #999;page-break-inside:avoid;} thead{display:table-header-group;} tr,img{page-break-inside:avoid;} img{max-width:100% !important;} @page {margin:0.5cm;}p,h2,h3{orphans:3;widows:3;} h2,h3{page-break-after:avoid;}}body{margin:0;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:13px;line-height:20px;color:#000000;background-color:#ffffff;}:' $(notebook).slides.html $<
# May not be needed anymore
# sed -i 's:class="fragment" class="text_cell_render:class="fragment text_cell_render:' $(notebook).reveal.html $<


