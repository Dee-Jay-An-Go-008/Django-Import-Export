
// <!-- delete_modal.js -->
// <script>
  $(document).ready(function () {
    $("#confirmDeleteFormModal").on("shown.bs.modal", function (event) {
      // Get the anchor element that triggered the modal
      var button = $(event.relatedTarget);

      // Extract the value from the 'data-url' attribute of the trigger button
      var urlValue = button.data("url");

      // Find the specific link within the modal and 
      // update its 'href' or 'action' attribute
      // var modalLink = $(this).find('#modal-dynamic-link');
      // modalLink.attr("href", urlValue);
      // or 
      // modalLink.attr("action", urlValue);

      $("#confirmDeleteFormForm").attr("action", urlValue);
    });
  });
// </script>