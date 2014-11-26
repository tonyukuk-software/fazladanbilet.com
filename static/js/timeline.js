var timeline = {
    selContainer: '.b-timeline',
    selBlock: '.b-timeline__block',
    selContent: '.b-timeline__content',
    selMarker: '.b-timeline__marker',

    init: function() {
        var me = this;

        if ($(me.selContainer).length > 0) {
            $(window).resize(function() {
                me.layoutTimeline();
            });
            me.layoutTimeline();
        }
    },

    layoutTimeline: function() {
        var me = this;

        $(me.selContainer).each(function() {
            var container = $(this);
            var isOneColumnLayout = true;
            //noinspection FunctionWithInconsistentReturnsJS
            $(me.selContent, container).each(function() {
                if ($(this).css('float') != 'none') {
                    isOneColumnLayout = false;
                    return false; // break
                }
            });

            var containerHeight = 0;
            $(me.selBlock, container).each(function() {
                var blockBottom = me.layoutBlock($(this), isOneColumnLayout);
                if (blockBottom > containerHeight) {
                    containerHeight = blockBottom;
                }
            });
            container.css({'height': containerHeight});
        });
    },

    layoutBlock: function(block, isOneColumnLayout) {
        var me = this;

        var prevBlock = block.prev();
        var top = 0; // first block should be positioned at top
        if (prevBlock.length > 0) {
            var upperBlock = prevBlock.prev();
            if (isOneColumnLayout) {
                // all blocks should be positioned next to prev block
                top = parseInt(prevBlock.css('top')) + prevBlock.outerHeight();
            } else if (upperBlock.length == 0) {
                // second block should be at right column
                top = parseInt(prevBlock.css('top')) + $(me.selMarker, prevBlock).outerHeight();
            } else {
                // after second block, all blocks should be positioned based on own column prev block position
                // and prev block marker (which is greater)
                var upperBottom = parseInt(upperBlock.css('top')) + upperBlock.outerHeight();
                var prevMarker = parseInt(prevBlock.css('top')) + $(me.selMarker, prevBlock).outerHeight();
                top = (upperBottom > prevMarker) ? upperBottom : prevMarker;
            }
        }
        block.css({'top': top, 'display': 'block'});

        return top + block.outerHeight();
    }
};
timeline.init();