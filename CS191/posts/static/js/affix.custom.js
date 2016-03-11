$(document).ready(function() {

	// Affix behavior for sidebar
	$('#topics').affix({
		offset: {
			top: ($('#topics').offset().top) - 20,
			bottom: ($('#topics').offset().bottom)
		}
	});

	$('[data-clampedwidth]').each(function () {
	    var elem = $(this);
	    var parentPanel = elem.data('clampedwidth');
	    var resizeFn = function () {
	    	var sideBarNavWidth = $(parentPanel).width();
	        elem.css('width', sideBarNavWidth);
	    };
	    resizeFn();
	    $(window).resize(resizeFn);
	});

	// Tooltip behavior for icons
	$('.hot-topic').tooltip({
		placement: 'bottom',
		title: 'Hot topic'
	})
	
});
