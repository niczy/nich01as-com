(function() {
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

  UpdateQuestionVisibility(0, 1);


  var showQuestion = false;
  $('.questions-wrapper').addClass('hidden');
  $('#toggle-question').click(function() {
    if (showQuestion) {
      $('.questions-wrapper').addClass('hidden');
      $('#toggle-question').html('Show Questions');
    } else {
      $('.questions-wrapper').removeClass('hidden');
      $('#toggle-question').html('Hide Questions');
    }
    showQuestion = !showQuestion;
  });
}());
