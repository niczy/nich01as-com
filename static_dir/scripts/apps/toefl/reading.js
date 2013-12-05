(function() {
  var currentQuestionIndex = 0;
  var questionsElements = $('.question');
  var UpdateQuestionVisibility = function(oldQuestionIndex, newQuestionIndex) {
    if (oldQuestionIndex == newQuestionIndex) {
      return;
    }
    $('.question-' + oldQuestionIndex).addClass('hidden');
    $('.question-' + newQuestionIndex).removeClass('hidden');
    $('.question-highlight-' + oldQuestionIndex).removeClass('highlight');
    $('.question-highlight-' + newQuestionIndex).addClass('highlight');
    currentQuestionIndex = newQuestionIndex;
    if (currentQuestionIndex == 1) {
      $('#previous-question').prop('disabled', true)
    } else {
      $('#previous-question').prop('disabled', false)
    }
    if (currentQuestionIndex == questionsElements.length) {
      $('#next-question').prop('disabled', true);
    } else {
      $('#next-question').prop('disabled', false);
    }
  };

  $('#next-question').click(function() {
    var newQuestionIndex = currentQuestionIndex;
    if (currentQuestionIndex < questionsElements.length) {
      newQuestionIndex = currentQuestionIndex + 1; 
    }
    UpdateQuestionVisibility(currentQuestionIndex, newQuestionIndex);
  });
  $('#previous-question').click(function() {
    var newQuestionIndex = currentQuestionIndex;
    if (currentQuestionIndex > 1) {
      newQuestionIndex = currentQuestionIndex - 1;
    }
    UpdateQuestionVisibility(currentQuestionIndex, newQuestionIndex);
  });
  $('#show-answers').click(function() {
    questionsElements.removeClass('hidden');
    $('.questions-wrapper').removeClass('hidden');
    $('#next-question').prop('disabled', true);
    $('#previous-question').prop('disabled', true);
    $('.right-answer').each(function(index, element) {
      if ($(element).is(':checked')) {
        $(element).parent().addClass('answer-correct');
      } else {
        $(element).parent().addClass('answer-wrong');
      }
    });
    $('.wrong-answer').each(function(index, element) {
      if ($(element).is(':checked')) {
        $(element).parent().addClass('answer-wrong');
      } 
    });
  });
  
}());
