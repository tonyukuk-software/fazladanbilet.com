jQuery.noConflict();

// Check to see which element to use to determine scrolling
if(jQuery.browser.msie || jQuery.browser.mozilla)
	{Screen = jQuery("html");}
else
	{Screen = jQuery("body");}


// Setup all the slider effects
var image_effects = {
	'image-left' : 'margin-left', 'image-only' : 'margin-bottom', 'image-right' : 'margin-right', 'image-title' : 'margin-bottom', 'text-only' : 'margin-bottom'
	};

var text_effects = {
	'image-left' : 'margin-right', 'image-only' : 'margin-top', 'image-right' : 'margin-left', 'image-title' : 'margin-top', 'text-only' : 'margin-top'
};

var $sliders;
jQuery(document).ready(function(){
	// Setup variables for DOM elements so that we only hit them once
	$sliders = jQuery('.slider ul').children("li.li-slide");
	$sliderarrows = jQuery(".slider-arrows");
	$slidercontent = jQuery(".slider-content");

	// Get the original positions of all the sliding elements
	arrpos = jQuery(".slider-arrows").css('top').toString().replace("px", "");
	bgTops = new Array();
	bgLefts = new Array();
	$sliders.each(function(){
		var bgpos = jQuery(this).css('backgroundPosition').toString();
		var stopper = bgpos.indexOf(' ');
		var len = bgpos.length;
		var left = bgpos.substring(0, stopper).replace("%", "");
		var top = bgpos.substring(stopper,len).replace("%", "");
		bgTops.push(top);
		bgLefts.push(left);
	});
});

jQuery(window).scroll(function(){
	// Get the Scroll size and set the opacity
	var scrolled = Screen.scrollTop();
	var total = Screen.height();
	var opacity = ((100-(scrolled/4))/65);

	$sliders.each(function(){
		i = jQuery(this).index();
		bgleft = bgLefts[i];
		bgtop = bgTops[i];
		var scrollPercent = (scrolled/total)*200;
		var bgpos = +scrollPercent + +bgtop;
		jQuery(this).css({'backgroundPosition': bgleft+'% '+bgpos+'%'});
	});

	// Change the opacity and the positioning of the following elements as we scroll
	$sliderarrows.css({'top': +arrpos-(scrolled*0.165), 'opacity': opacity});
	$slidercontent.css({'top': -(scrolled/6.25), 'opacity': opacity});
});

// Auto-slider clearer
function clear_auto_slide(){
	jQuery("div[id^='slider-auto']").each(function(){
		if(!isNaN(jQuery(this).text()) && jQuery(this).text() !== "0" && jQuery(this).text() !== "")
			{clearInterval(SliderInterval);}
	});
}
function doSlider(direction){

	i = jQuery('.slider ul').children("li.active").index();
	max = ($sliders.size()-1);
	if(direction == 1) {
		j = (i+1);
		if(i == max)
			j = 0;
	} else{
		j = (i-1);
		if(i == 0)
			j = max;
	}

	// Elements to fade out
	previousslide = $sliders.eq(i);
	previousslide.fadeOut().removeClass("active");
	sliderclass = previousslide.children('.slider-content').attr("data-class");

	var options = {};
	image_effect = image_effects[sliderclass];
	options['opacity'] = 1;
	options[image_effect] = '-25px';
	previousslide.children('.slider-content').children('.slider-image').animate(options, {duration: 300}, {easing: 'swing'});

	var options = {};
	options['opacity'] = 1;
	text_effect = text_effects[sliderclass];
	options[text_effect] = '-25px';
	previousslide.children('.slider-content').children('.slider-copy').animate(options, {duration: 300}, {easing: 'swing'});

	// Elements to fade in
	nextslide = $sliders.eq(j);
	sliderclass = nextslide.children('.slider-content').attr("data-class");
	nextslide.fadeIn({duration: 1000}).addClass("active");

	var options = {};
	options['opacity'] = 1;
	image_effect = image_effects[sliderclass];
	options[image_effect] = '0px';
	nextslide.children('.slider-content').children('.slider-image').animate(options, {duration: 650}, {easing: 'swing'});

	var options = {};
	options['opacity'] = 1;
	text_effect = text_effects[sliderclass];
	options[text_effect] = '0px';
	nextslide.children('.slider-content').children('.slider-copy').animate(options, {duration: 650}, {easing: 'swing'});
}


jQuery(document).ready(function(){
		sliderclass =$sliders.eq(0).children('.slider-content').attr("data-class");
		firstslide = $sliders.eq(0);

		var options = {};
		options['opacity'] = 1;
		image_effect = image_effects[sliderclass];
		options[image_effect] = '0px';
		firstslide.children('.slider-content').children('.slider-image').animate(options, {duration: 650}, {easing: 'swing'});

		var options = {};
		options['opacity'] = 1;
		text_effect = text_effects[sliderclass];
		options[text_effect] = '0px';
		firstslide.children('.slider-content').children('.slider-copy').animate(options, {duration: 650}, {easing: 'swing'});

		// Feature Auto-slide
		jQuery("div[id^='slider-auto']").each(function(){

			if(!isNaN(jQuery(this).text()) && jQuery(this).text() !== "0" && jQuery(this).text() !== "")
				{
					SliderInterval = setInterval(function(){

					doSlider(1);

					}, (jQuery(this).text()*1000));
				}
		});

		jQuery(".slider-arrows .previous").click(function(){
			clear_auto_slide();
			doSlider(0);
			return false;
		});

		jQuery(".slider-arrows .next").click(function(){
			clear_auto_slide();
			doSlider(1);
			return false;
		});
});
