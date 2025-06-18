$(document).ready(function () {
  if (window.location.href.indexOf("/dataset/new") !== -1) {
    var nameField = $("#field-name");
    if (nameField.length && !nameField.val()) {
      var randomName = Math.floor(10000 + Math.random() * 90000).toString();
      nameField.val(randomName);
    }
  }
});
