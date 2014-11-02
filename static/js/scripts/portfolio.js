function slideFrame(container, direction)
	{
		/* Set the new position & frame number */
		move_by = container.parent().width();
		frame_left = container.css('left').replace("px", "");
		frame = Math.round(-(frame_left/move_by));
		maxsize = (container.children("li").size()-1);

		if(direction == 0)
			{
				new_frame = +frame+1;
				if(maxsize <= frame)
					new_frame = 0;
			}
		else
			{
				new_frame = +frame-1;
				if(frame == 0)
					new_frame = maxsize;
			}

		// Do the sliding action
		container.animate({"left": -(new_frame*(move_by))}, {duration: 350});

		// Match the height
		var useheight = $gallerycontainer.children("li").eq(new_frame).children("a").children("img").height();
		$galleryslider.css({height: useheight}, 250);
	}


function resize_slide(element){

	if(element.children("ul").css("left") == undefined){
		return false;
	}

	var container = element.children("ul");
	var width = element.width();
	var left = element.children("ul").css("left").replace("px", "");

	if(isNaN(left))
		var frame = 0;
	else
		var frame = Math.round(width/-(left));

	if(container.children("li").length > 0){
		container.children("li").css({'width': width});
		container.css({'left': -(frame*width)});
	} else {
	 	var frame = 0;
	}

	if($gallerycontainer.children("li").eq(frame) !== undefined)
		return true;

	theli = $gallerycontainer.children("li").eq(frame);
	if(theli.html().toString().indexOf("<img") > -1){
		jQuery(".gallery-slider, .gallery-slider .portfolio-image").animate({height: (useheight)}, 250);
	};
}


jQuery(window).resize(function(){
	resize_slide($galleryslider);
	if(jQuery(document).width() > 600){
		jQuery("#nav").show();
	}
});

jQuery(document).ready(function()
	{
		if(jQuery.browser.msie || jQuery.browser.mozilla)
			{Screen = jQuery("html");}
		else
			{Screen = jQuery("body");}

		$galleryslider = jQuery(".gallery-slider");
		$gallerycontainer = $galleryslider.children("ul");
		$gallerycontainer.animate({"left": 0}, {duration: 500});
		resize_slide($galleryslider);

		jQuery(".gallery-slider .next").bind("click", function(){
			slideFrame($gallerycontainer, 0);
			return false;
		});

		jQuery(".gallery-slider .previous").bind("click", function(){
			slideFrame($gallerycontainer, 1);
			return false;
		});
});
