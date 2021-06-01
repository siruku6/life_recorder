let AutocompleteModule = {
  candidates: $('#autocomplete-candidates > li.candidate')
    .map(function(_i, candidate) { return candidate.innerText })
    .get(),
  filterCandidatesBy: function(inputKeywords) {
    let candidatesArray = AutocompleteModule.candidates.slice();
    $.each(inputKeywords, function(_, keyword) {
      let regX = new RegExp(keyword, 'i');
      candidatesArray = candidatesArray.filter(function(candidate) {
        return regX.test(candidate);
      });
    });
    return candidatesArray;
  },
  highlightMatchedChars: function() {
    const suggestedList = $("ul.ui-autocomplete > li.ui-menu-item > .ui-menu-item-wrapper");
    const searchTerm = $.trim($("#activity-name").val()).split(/\s+/).join('|');
    let regX = new RegExp('(' + searchTerm + ')', "ig");

    suggestedList.each(function() {
      let $this = $(this);
      let oldOption = $this.text();
      $this.html(oldOption.replace(regX, '<span class="autocomplete-custom-highlight">$1</span>'));
    });
  },
}

$(function() {
  $('#activity-name').autocomplete({
    source:  function(requestObj, responseFunc) {
      const inputKeywords = requestObj.term.split(/\s+/);
      let filteredCandidates = AutocompleteModule.filterCandidatesBy(inputKeywords)
      return responseFunc(filteredCandidates);
    },
    open: function(_event, _ui) {
      AutocompleteModule.highlightMatchedChars();
    },
    focus: function (_event, _ui) {
      return false;
    },
    // delay: 500,
    minLength: 1
  });
});
