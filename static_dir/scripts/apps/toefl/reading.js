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
(function() {
  var countDown = 20 * 60;
  var timerState = 'pause';
  var countingDownInterval;
  $('#timer-start').click(function() {
    if (timerState == 'pause') {
      timerState = 'running';
      $('#timer-start').text('Pause');
        countingDownInterval = setInterval(function() {
        countDown = countDown - 1;
        if (countDown == 0) {
          clearInterval(countingDownInterval);
        } else {
          var reminder = countDown % 60;
          var reminderStr = reminder >= 10 ? reminder : '0' + reminder;
          $('#time').text(Math.floor(countDown / 60) + ":" + reminderStr);
        }
      }, 1000);
    } else {
      timerState = 'pause';
      $('#timer-start').text('Start');
      clearInterval(countingDownInterval);
    }
  });
  $('#timer-reset').click(function() {
    clearInterval(countingDownInterval);
    countDown = 20 * 60;
    $('#time').text('20:00');
    timerState = 'pause';
    $('#timer-start').text('Start');
  });
}());
