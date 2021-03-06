(function($){
    "use strict";

    // Dropdown on mouse hover
$(document).ready(function () {
    function toggleNavbarMethod() {
        if ($(window).width() > 992) {
            $('.navbar .dropdown').on('mouseover', function () {
                $('.dropdown-toggle', this).trigger('click');
            }).on('mouseout', function () {
                $('.dropdown-toggle', this).trigger('click').blur();
            });
        } else {
            $('.navbar .dropdown').off('mouseover').off('mouseout');
        }
    }
    toggleNavbarMethod();
    $(window).resize(toggleNavbarMethod);
});

})(jQuery);


copy =(element) => {
    document.getElementById(element).select();
    document.execCommand("copy");
           }

function scrollTo() {
   const links = document.querySelectorAll('.scroll');
   links.forEach(each => (each.onclick = scrollAnchors));
}

function scrollAnchors(e, respond = null) {
   const distanceToTop = el => Math.floor(el.getBoundingClientRect().top);
   e.preventDefault();
   var targetID = (respond) ? respond.getAttribute('href') : this.getAttribute('href');
   const targetAnchor = document.querySelector(targetID);
   if (!targetAnchor) return;
   const originalTop = distanceToTop(targetAnchor);
   window.scrollBy({ top: originalTop, left: 0, behavior: 'smooth' });
   const checkIfDone = setInterval(function() {
       const atBottom = window.innerHeight + window.pageYOffset >= document.body.offsetHeight - 2;
       if (distanceToTop(targetAnchor) === 0 || atBottom) {
           targetAnchor.tabIndex = '-1';
           targetAnchor.focus();
           window.history.pushState('', '', targetID);
           clearInterval(checkIfDone);
       }
   }, 3000);
}
