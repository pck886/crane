jQuery(document).ready(function($) {

    $("div[name^='myCarousel-']").carousel({
        interval: 5000
    });

    //Handles the carousel thumbnails
    $('[id^=carousel-selector-]').click(function () {
        var id_selector = $(this).attr("id");
        var parent_id_selector = $(this).parent().parent().parent().attr("id");
        try {
            var parent_id = /-(\d+)$/.exec(parent_id_selector)[1];
            var id = /-(\d+)$/.exec(id_selector)[1];
            console.log(id_selector, id);
            $("div[name^=" + 'myCarousel-'+parent_id + "]").carousel(parseInt(id));
        } catch (e) {
            console.log('Regex failed!', e);
        }
    });

    // When the carousel slides, auto update the text
    $("div[name^='myCarousel-']").on('slid.bs.carousel', function (e) {
        var id = $(this).find('.item.active').data('slide-number');
        $('#carousel-text').html($('#slide-content-'+id).html());
    });
});