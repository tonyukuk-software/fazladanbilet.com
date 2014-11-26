$(document).ready(function(){

    new jPlayerPlaylist({
        jPlayer: "#jquery_jplayer_1",
        cssSelectorAncestor: "#jp_container_1",
        cssSelector: {
            stop: ''
        }
    }, [
        {
            title:"Cyber Sonnet",
            mp3:"audio/TSP-07-Cybersonnet.mp3",
            oga:"audio/TSP-07-Cybersonnet.ogg"
        },
        {
            title:"Thin Ice",
            mp3:"audio/Miaow-10-Thin-ice.mp3",
            oga:"audio/Miaow-10-Thin-ice.ogg"
        },
        {
            title:"Your Face",
            mp3:"audio/TSP-05-Your_face.mp3",
            oga:"audio/TSP-05-Your_face.ogg"
        }
    ], {
        swfPath: "js",
        supplied: "oga, mp3",
        wmode: "window",
        smoothPlayBar: true,
        keyEnabled: true
    });

    new jPlayerPlaylist({
        jPlayer: "#jquery_jplayer_2",
        cssSelectorAncestor: "#jp_container_2",
        cssSelector: {
            stop: ''
        }
    }, [
        {
            title:"Lismore",
            mp3:"audio/Miaow-04-Lismore.mp3",
            oga:"audio/Miaow-04-Lismore.ogg"
        },
        {
            title:"Beside Me",
            mp3:"audio/Miaow-06-Beside-me.mp3",
            oga:"audio/Miaow-06-Beside-me.ogg"
        }
    ], {
        swfPath: "js",
        supplied: "oga, mp3",
        wmode: "window",
        smoothPlayBar: true,
        keyEnabled: true
    });

    new jPlayerPlaylist({
        jPlayer: "#jquery_jplayer_3",
        cssSelectorAncestor: "#jp_container_3",
        cssSelector: {
            stop: ''
        }
    }, [

        {
            title:"Stirring of a Fool",
            mp3:"audio/Miaow-08-Stirring-of-a-fool.mp3",
            oga:"audio/Miaow-08-Stirring-of-a-fool.ogg"
        },
        {
            title:"Partir",
            free: true,
            mp3:"audio/Miaow-09-Partir.mp3",
            oga:"audio/Miaow-09-Partir.ogg"
        }
    ], {
        swfPath: "js",
        supplied: "oga, mp3",
        wmode: "window",
        smoothPlayBar: true,
        keyEnabled: true
    });

});