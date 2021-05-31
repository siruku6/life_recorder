$(function(){
  const candidates = [
    'ruby',
    'python',
    'c',
    'c++',
    'c#',
    'php',
    'go-lang',
    'Lisp',
  ];

  $('#activity-name').autocomplete({
    source:  function(requestObj, responseFunc) {
      let candidatesArray = candidates.slice();
      const inputKeywords = requestObj.term.split(/\s+/);
 
      $.each(inputKeywords, function(_, keyword) {
        let regX = new RegExp(keyword, 'i');
        candidatesArray = candidatesArray.filter(function(candidate) {
          return regX.test(candidate);
        });
      });
      
      return responseFunc(candidatesArray);
    },
    open: function(_event, _ui) {
      // INFO: highlight matched characters in yellow
      const suggestedList = $("ul.ui-autocomplete > li.ui-menu-item > .ui-menu-item-wrapper");
      const searchTerm = $.trim($("#activity-name").val()).split(/\s+/).join('|');
      let regX = new RegExp('(' + searchTerm + ')', "ig");

      suggestedList.each(function() {
        let $this = $(this);
        let oldOption = $this.text();
        $this.html(oldOption.replace(regX, '<span class="autocomplete-custom-highlight">$1</span>'));
      });
    },
    focus: function (_event, _ui) {
      return false;
    },
    // delay: 500,
    minLength: 2
  });
});
