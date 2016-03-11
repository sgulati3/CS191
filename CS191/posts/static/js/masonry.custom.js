// init Masonry
var $grid = $('.masonry').masonry({
	columnWidth: 100,
	itemSelector: '.masonry-item',
	percentPosition: true,
	fitWidth: true,
	gutter: 10
});

// layout Masonry after each image loads
$grid.imagesLoaded().progress( function() {
  	$grid.masonry('layout');
});
