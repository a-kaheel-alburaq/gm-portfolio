/**
* Template Name: Ninestars - v2.0.0
* Template URL: https://bootstrapmade.com/ninestars-free-bootstrap-3-theme-for-creative/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

!(function ($) {
  "use strict";

  // Smooth scroll for the navigation menu and links with .scrollto classes
  $(document).on('click', '.nav-menu a, .mobile-nav a, .scrollto', function (e) {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      e.preventDefault();
      var target = $(this.hash);
      if (target.length) {

        var scrollto = target.offset().top;

        if ($('#header').length) {
          scrollto -= $('#header').outerHeight();
        }

        if ($(this).attr("href") == '#header') {
          scrollto = 0;
        }

        $('html, body').animate({
          scrollTop: scrollto
        }, 1500, 'easeInOutExpo');

        if ($(this).parents('.nav-menu, .mobile-nav').length) {
          $('.nav-menu .active, .mobile-nav .active').removeClass('active');
          $(this).closest('li').addClass('active');
        }

        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
          $('.mobile-nav-overly').fadeOut();
        }
        return false;
      }
    }
  });

  // Mobile Navigation
  if ($('.nav-menu').length) {
    var $mobile_nav = $('.nav-menu').clone().prop({
      class: 'mobile-nav d-lg-none'
    });
    $('body').append($mobile_nav);
    $('body').prepend('<button type="button" class="mobile-nav-toggle d-lg-none"><i class="icofont-navigation-menu"></i></button>');
    $('body').append('<div class="mobile-nav-overly"></div>');

    $(document).on('click', '.mobile-nav-toggle', function (e) {
      $('body').toggleClass('mobile-nav-active');
      $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
      $('.mobile-nav-overly').toggle();
    });

    $(document).on('click', '.mobile-nav .drop-down > a', function (e) {
      e.preventDefault();
      $(this).next().slideToggle(300);
      $(this).parent().toggleClass('active');
    });

    $(document).click(function (e) {
      var container = $(".mobile-nav, .mobile-nav-toggle");
      if (!container.is(e.target) && container.has(e.target).length === 0) {
        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
          $('.mobile-nav-overly').fadeOut();
        }
      }
    });
  } else if ($(".mobile-nav, .mobile-nav-toggle").length) {
    $(".mobile-nav, .mobile-nav-toggle").hide();
  }

  // Back to top button
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $('.back-to-top').fadeIn('slow');
    } else {
      $('.back-to-top').fadeOut('slow');
    }
  });

  $('.back-to-top').click(function () {
    $('html, body').animate({
      scrollTop: 0
    }, 1500, 'easeInOutExpo');
    return false;
  });

  // Porfolio isotope and filter
  $(window).on('load', function () {
    var portfolioIsotope = $('.portfolio-container').isotope({
      itemSelector: '.portfolio-item',
      layoutMode: 'fitRows'
    });

    $('#portfolio-flters li').on('click', function () {
      $("#portfolio-flters li").removeClass('filter-active');
      $(this).addClass('filter-active');

      portfolioIsotope.isotope({
        filter: $(this).data('filter')
      });
    });

    // Initiate venobox (lightbox feature used in portofilo)
    $(document).ready(function () {
      $('.venobox').venobox();
    });
  });

  // Clients carousel (uses the Owl Carousel library)
  $(".clients-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    autoplayTimeout: 1000, // Adjust speed
    autoplayHoverPause: true, // Pause on hover
    responsive: {
      0: {
        items: 2
      },
      768: {
        items: 4
      },
      900: {
        items: 5
      }
    }
  });

  // Initi AOS
  AOS.init({
    duration: 800,
    easing: "ease-in-out"
  });

})(jQuery);

//Card open and close in Vission Mission and Values 
document.querySelectorAll('.toggle-details').forEach(toggle => {
  toggle.addEventListener('click', function () {
    const card = this.closest('.card-expandable');
    const arrow = this.querySelector('.arrow-circle');

    card.classList.toggle('active');

    if (card.classList.contains('active')) {
      arrow.classList.remove('fa-chevron-down');
      arrow.classList.add('fa-chevron-up');
    } else {
      arrow.classList.remove('fa-chevron-up');
      arrow.classList.add('fa-chevron-down');
    }
  });
});
document.addEventListener('DOMContentLoaded', function () {
  // Get the carousel element
  const myCarousel = document.querySelector('#heroCarousel');

  // Check if the carousel element exists
  if (myCarousel) {
    const carousel = new bootstrap.Carousel(myCarousel);

    // Get all the custom indicator buttons
    const customIndicators = document.querySelectorAll('.custom-indicators button');

    // Add event listeners for each custom indicator button
    customIndicators.forEach((button, index) => {
      button.addEventListener('click', () => {
        // Navigate to the corresponding slide
        carousel.to(index);

        // Update the active class on the buttons
        customIndicators.forEach((btn) => btn.classList.remove('active'));
        button.classList.add('active');
      });
    });

    // Optionally, sync the active class on page load
    myCarousel.addEventListener('slide.bs.carousel', (event) => {
      const currentIndex = event.to; // The index of the new slide
      customIndicators.forEach((button, index) => {
        if (index === currentIndex) {
          button.classList.add('active');
        } else {
          button.classList.remove('active');
        }
      });
    });
  } else {
    console.error('Carousel element not found');
  }
});


//video
document.addEventListener("DOMContentLoaded", function () {
  const videoButton = document.getElementById("play-video");
  const modal = document.getElementById("video-modal");
  const closeButton = document.getElementById("close-video");
  const video = document.getElementById("internal-video");

  // Open video modal
  videoButton.addEventListener("click", function (e) {
    e.preventDefault();  // Prevent any default action
    modal.style.display = "flex"; // Show modal
    video.play(); // Play the video
  });

  // Close video modal
  closeButton.addEventListener("click", function () {
    video.pause(); // Pause video
    video.currentTime = 0; // Reset video
    modal.style.display = "none"; // Hide modal
  });
});

//Brief sectoin Counter Animation
// Counter animation
document.addEventListener('DOMContentLoaded', function () {
  const counters = document.querySelectorAll('.counter');

  function animateCounter(counter) {
    const target = +counter.getAttribute('data-target');
    let count = 0;
    const speed = target / 200;  // Adjust speed to control how fast the counter increases

    const interval = setInterval(() => {
      count += speed;
      if (count >= target) {
        count = target;
        clearInterval(interval);
      }
      counter.innerText = Math.floor(count);  // Show the integer part of the count
    }, 10);  // Adjust the delay to control the speed of the counting
  }

  // Observer to trigger counters once the section is in view
  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const counterElement = entry.target.querySelector('.counter');
        if (counterElement) {
          animateCounter(counterElement);  // Trigger counter animation
        }
        observer.unobserve(entry.target);  // Stop observing after the animation starts
      }
    });
  }, { threshold: 0.5 });  // When 50% of the section is in view, start the animation

  // Observe each stats-box
  document.querySelectorAll('.stats-box').forEach((box) => {
    observer.observe(box);
  });
});

$(document).ready(function () {
  $('#careers-carousel').owlCarousel({
    loop: true,
    margin: 10,
    dots: true, // Ensure this is set to true
    autoplay: true,
    autoplayHoverPause: true, // Pause on hover
    autoplayTimeout: 1000,
    responsive: {
      0: { items: 1 },
      768: { items: 2 },
      1024: { items: 3 }
    }
  });
});

// Scroll Progress Bar
window.onscroll = function () {
  // Calculate scroll percentage
  let scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
  let docHeight = document.documentElement.scrollHeight || document.body.scrollHeight;
  let winHeight = window.innerHeight || document.documentElement.clientHeight;
  let scrollPercent = (scrollTop / (docHeight - winHeight)) * 100;

  // Update progress bar height
  let progressBar = document.querySelector('#scroll-progress-bar::after');
  progressBar.style.height = scrollPercent + '%';

  // Update progress bar color based on scroll position (show remaining page)
  if (scrollPercent < 50) {
    progressBar.style.backgroundColor = '#ffad42'; // Yellow for top half
  } else {
    progressBar.style.backgroundColor = '#ff0000'; // Red for bottom half
  }
};


window.onscroll = function () {
  // Get scroll position and document height
  let scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
  let docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;

  // Calculate scroll percentage
  let scrollPercent = (scrollTop / docHeight) * 100;

  // Select the progress bar and back-to-top button
  let progressBar = document.getElementById("scroll-progress-bar");
  let backToTop = document.getElementById("back-to-top");

  // Update progress bar gradient
  progressBar.style.background = `linear-gradient(to top, #fdb417 ${scrollPercent}%, black ${scrollPercent}%)`;

  // Toggle visibility based on scroll position
  if (scrollTop > 50) {
    progressBar.style.opacity = "1"; // Show the bar
    backToTop.style.opacity = "1"; // Show the button
  } else {
    progressBar.style.opacity = "0"; // Hide the bar
    backToTop.style.opacity = "0"; // Hide the button
  }
};

// Scroll to top function
function scrollToTop() {
  window.scrollTo({ top: 0, behavior: "smooth" });
}

$(document).ready(function () {
  $("#careers-carousel-2lines").owlCarousel({
    items: 1,  // One item per slide
    loop: true,  // Infinite loop
    margin: 10,  // Space between items
    nav: false,  // Disable arrows
    dots: true,  // Enable dots navigation
    autoplay: true,  // Enable autoplay
    autoplayTimeout: 1000,  // 1 seconds for each slide
    autoplayHoverPause: true  // Pause autoplay on hover
  });
});
console.log("hello")