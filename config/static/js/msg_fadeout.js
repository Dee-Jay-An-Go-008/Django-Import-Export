
//<!-- message fadeout js script -->

  // set message to fade out after 3 to 10 seconds
  // need to collectstatic after making changes to static files
  // python manage.py collectstatic
  // runserver will serve static files in development mode
  // in production, need to configure web server to serve static files
  // for example, using nginx or apache
  // also need to set STATIC_URL and STATIC_ROOT in settings.py
  // STATIC_URL = '/static/'
  // STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
  // then run collectstatic to collect static files into STATIC_ROOT
  // finally, configure web server to serve files from STATIC_ROOT at STATIC_URL
  setTimeout(() => {
    $("#djmessage").fadeOut("slow");
  }, 3000);
  setTimeout(function () {
    $("#djmessage1").fadeOut("slow");
  }, 6000);
  setTimeout(function () {
    $("#djmessage2").fadeOut("slow");
  }, 8000);
  setTimeout(function () {
    $("#djmessage3").fadeOut("slow");
    $("#djmessage4").fadeOut("slow");
    $("#djmessage5").fadeOut("slow");
    $("#djmessage6").fadeOut("slow");
    $("#djmessage7").fadeOut("slow");
    $("#djmessage8").fadeOut("slow");
    $("#djmessage9").fadeOut("slow");
    $("#djmessage10").fadeOut("slow");
  }, 10000);
