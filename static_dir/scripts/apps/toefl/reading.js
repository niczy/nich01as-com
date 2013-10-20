(function() {
  var currentQuestionIndex = -1;
  var questionsElements = $('.question');
  var UpdateQuestionVisibility = function() {
    questionsElements.removeClass(function(index, oldClass) {
      return index == currentQuestionIndex ? 'hidden' : '';
    }).addClass(function(index, oldClass) {
      return index == currentQuestionIndex ? '' : 'hidden';
    });
  };

  $('#next-question').click(function() {
    if (currentQuestionIndex + 1 < questionsElements.length) {
      currentQuestionIndex = currentQuestionIndex + 1; 
    }
    UpdateQuestionVisibility();
  });
  $('#previous-question').click(function() {
    if (currentQuestionIndex > 0) {
      currentQuestionIndex = currentQuestionIndex - 1;
    }
    UpdateQuestionVisibility();
  });
  $('#show-answers').click(function() {
    questionsElements.removeClass('hidden');
    $('#next-question').prop('disabled', true);
    $('#previous-question').prop('disabled', true);
    $('.right-answer').each(function(index, element) {
      if ($(element).is(':checked')) {
        $(element).parent().addClass('answer-correct');
      } else {
        $(element).parent().addClass('answer-wrong');
      }
    });
  });

  $('#back-to-list').click(function() {
    window.location.href= "/toefl/reading";
  });
}());
