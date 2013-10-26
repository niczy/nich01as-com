(function(){
  var editParagraphContainerElement = $("#paragraph-edit-container");
  var paragraphElement = $("#edit-paragraph");
  var articleElement = $("#article");
  var addParagraphButton = $("#add-paragraph");
  var addQuestionButton = $("#add-question");
  var questionsContainerDiv = $("#questions-container");
  
  addParagraphButton.click(function() {
    if (editParagraphContainerElement.hasClass("hidden")) {
      editParagraphContainerElement.removeClass("hidden");
      addParagraphButton.text("Done");
    } else {
      editParagraphContainerElement.addClass("hidden");
      addParagraphButton.text("Add Paragraph");
      console.log(paragraphElement.val());
      articleElement.append($("<p>").text(paragraphElement.val()));
      paragraphElement.val("");
    }
  });

  addQuestionButton.click(function() {
    var questionDiv = $('<div class="question"></div>');
    var optionsContainerDiv = $('<div class="options-container"></div>');
    var descriptionTextArea = $("<textarea>");
    var addOptionButton = $('<button class="btn btn-default">Add Option</button>');;

    var referParagraph = $('<div class="context"><label>Refered paragraphs:</label> <input class="refer-paragraph" type="text"></input></div>');

    var highlightWordOrSentense = $('<div class="context"><label>Highlited word or sentense:</label><input class="hight-word-sentense" type="text"></input></div>');

    
    questionDiv.append(descriptionTextArea);
    questionDiv.append(optionsContainerDiv);
    questionDiv.append(addOptionButton);
    questionDiv.append(referParagraph);
    questionDiv.append(highlightWordOrSentense);

    questionsContainerDiv.append(questionDiv);

    addOptionButton.click(function(){
      var optionContainer = $('<div class="option"></div>');
      var optionInput = $('<input type="text" class="option-des"></input>');
      var correctAnswerCheckbox = $('<div class="correct-option">Is Correct Option? <input type="checkbox" class="is-correct-option"></input></div>');
      var removeSpan = $('<span class="option-remove">remove</span>');

      optionContainer.append(optionInput);
      optionContainer.append(removeSpan);
      optionContainer.append(correctAnswerCheckbox);
      optionsContainerDiv.append(optionContainer);
      removeSpan.click(function() {
        optionContainer.remove();
      });
    });

  });

}());
