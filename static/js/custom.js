$(document).ready(function(){

  $('.carousel').carousel();
  $('#questions-caorusel').carousel({ interval : false });
  $('*[data-toggle]').tooltip();
  $('.promo-login-trigger').click(function(){
    $('.promo-login').toggleClass('hidden');
  });

  // console.log( $(window).height() );

  $(".openimg").colorbox();

  // textarea filling
  $('.adcom').each(function(){
    var ta = $(this).find('textarea[maxlength]');

    ta.keyup(function(){
        var max = parseInt($(this).attr('maxlength'));
        if($(this).val().length > max){
            $(this).val($(this).val().substr(0, $(this).attr('maxlength')));
        } else if ($(this).val().length === max){
            $(this).parent().find('.charsRemaining').addClass('full');
        } else if ($(this).val().length < max) {
            $(this).parent().find('.charsRemaining').removeClass('full');
        }
        $(this).parent().find('.charsRemaining').html((max - $(this).val().length) + ' characters remaining');
    });

    ta.parent().find('.attach-btn').click(function(){
      $(this).next('.attach').toggleClass('active'); 
      !$('.overhead').hasClass('active') ? $('.overhead').addClass('active') : '';
      ta.parent().find('.btm-btn').css({'display': 'block'});
      ta.addClass('wasActive');
    });  

    ta.on('focus',function(){
      $(this).addClass('wasActive');
      $('.overhead').addClass('active');
      $(this).css({ height: '90px' });
      $(this).parent().find('.btm-btn').css({'display': 'block'});
    });

    $('.overhead').click(function(){
      $(this).removeClass('active');
      if ( ta.hasClass('wasActive') && ta.val().length < 1 && ta.parent().find('.attach input').val().length < 1 ){
        ta.css({ height: '20px' });
        ta.parent().find('.btm-btn').css({'display': 'none'});
        ta.parent().find('.attach').removeClass('active');
        ta.removeClass('wasActive');
      } 
    });

  });

  $('.add-img-wrapper input[type="file"]').on('change', function(){
    var fname = $(this).val().split("\\").pop();
    $(this).closest('.attach').find('input[name="media_url"]').val("upload image: " + fname);
    $(this).closest('.attach').find('select[name="media_url"]').val('IMAGE');
  })


  $('.comments-prev').click(function(){
    $(this).toggleClass('more-on');
    if ( $(this).hasClass('more-on') ) {
      $(this).html('Hide comments');
    } else {
      $(this).html('Load more comments');
    }
    $(this).parent().next('.more-comments').toggleClass('hidden');
  });

  /* Comment focus with the comment icon */
  $('.comment-it').click(function(){
    $(this).closest('.entry-info').next('.comments').find('.add-comment textarea').focus();
  });

  /* Upload avatar */
  $('.selectFile').find('input[type="file"]').on('change', function(){
    var fName = $(this).val();
    $('.uploadButton').toggleClass('block');
    $(this).parent().toggleClass('hidden');
    $(this).parent().next('.sendFile').toggleClass('hidden');
    // $(this).parent().next('.sendFile').find('.filename').html(fName);
    $(this).parent().next('.sendFile').find('input[type="submit"]').focus();
  });

  $('#diary_form .bootstrap-tagsinput').on('click', function(){
    $(this).addClass('active');
    $(this).find('input').each(function(){
      $(this).on('blur', function(){
        $(this).parent().removeClass('active');
      });
    });
  });
  $('#diary_form .bootstrap-tagsinput input[type="text"]').focus(function(){
    $(this).parent().addClass('active');
  }).blur(function(){
    $(this).parent().removeClass('active');
  });

}); 

