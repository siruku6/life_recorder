$(function(){
  const programmingLanguages = [
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
    source: programmingLanguages
  });
});
