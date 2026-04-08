/* 4 features
1. Nav scroll effect
2. Answer button lock (prevents double clicks)
3. Seleced button highlight
4. Staggered results animation */

"use strict";

// A shortcut so we don't have to type document.queryselector every time .qs("#myid") is much cleaner
const qs = (selector) => document.querySelector(selector);
const qsa = (selector) => [...document.querySelectorAll(selector)];

// - Feature 1. Nav scroll effect - adds a CSS class to the nav when the user scrolls down. the class makes the background more opaque so content behind it doesn't bleed through.
// { passive: true} is a performance hint - it tells the browser this listener will never call preventDefault(). so it can scroll without waiting for JS to finish 

(function initNavScroll() {
    const nav = qs(".nav");
    if (!nav) return;
    window.addEventListener("scroll", () => {
        if (window.scrollY > 20) {
            nav.style.background = "rgba(15, 15, 20, 0.98)";
            nav.style.boxShadow = "0 4px 24px rgba(0, 0, 0, 0.4)";
        } else {
            nav.style.background = "rgba(15, 15, 20, 0.8)";
            nav.style.boxShadow = "none";
        }
    }, { passive: true });
})();

// - Feature 2 and 3. Answer button lock + selected highlighted. 
//Current problem - if a user clicks an answer, and then quickly clicks again before the page reloads, the form submits twice, which skips a questions.
//Fix - as soon as an answer is clicked, it immediately disable all button and highlights the chosen one. the form then submits normally.

function initAnswerButtons() {
  const form    = qs("#quizForm");
  const options = qsa(".quiz__option");
 
  if (!form || !options.length) return;
 
  options.forEach(button => {
    button.addEventListener("click", function() {
       options.forEach(btn => {
    
        if (btn !== this) {
          btn.disabled        = true;
          btn.style.opacity   = "0.4";
          btn.style.cursor    = "not-allowed";
          btn.style.transform = "none";
        }
      });
 
      this.style.opacity     = "1";
      this.style.borderColor = "var(--accent)";
      this.style.background  = "var(--accent-glow)";
      this.style.cursor      = "default";
      this.style.transform   = "scale(0.98)";
    });
  });
}();

// Feature 4 - staggered results animation. On the results page, ease answer review row animates in one after instead of all appearing at once. A css animation delay will be needed.

(function initResultsStagger() {
    const reviewItems = qsa(".review-item");
    if (!reviewItems.length) return; 

    reviewItems.forEach((item,index) => {
        item.style.opacity = "0";
        item.style.transform = "translateY(16px)";

        setTimeout(() => {
            item.style.transition = "opacity 0.4s ease, transform 0.4s ease";
            item.style.opacity = "1";
            item.style.transform = "none";
        }, index * 80);
    });
})();

// Feature 5 - Feedback form.

(function initFeedbackForm () {
    const form = qs("#feedbackForm");
    const successMessage = qs("#successMessage");
    const feedbackCard = qs("#feedbackCard");
    const submitBtn = qs("#submitBtn");

    if (!form) return;
    function validate() {
        let valid = true;
        
        qs("#nameError").textContent = "";
        qs("#ratingError").textContent = "";
        qs("#commentError").textContent = "";
        qs("#name").classList.remove("invalid");
        qs("#comment").classList.remove("invalid");

        if (!qs("#name").value.trim()) {
            qs("#nameError").textContent = "Please enter your name.";
            qs("#name").classList.add("invalid");
            valid = false;
        }

        const ratingSelected = document.querySelector('input[name="rating"]:checked');
        if (!ratingSelected) {
            qs("#ratingError").textContent = "Please select a rating.";
            qs("#starRating").classList.add("invalid");
            valid = false;
        } else {
            qs("#starRating").classList.remove("invalid");
        }

        if (!qs("#comment").value.trim ()) {
            qs("#commentError").textContent = "Please leave a comment.";
            qs("#comment").classList.add("invalid");
            valid = false;
        }

        return valid;
    }

    form.addEventListener("submit", async function(e) {
        e.preventDefault();
        if(!validate()) return;

        submitBtn.disabled = true;
        submitBtn.textContent = "Sending...";

        try {
            const response = await fetch("/feedback", {
                method: "POST",
                body: new FormData(form),
            });

            const data = await response.json();

            if (data.success) {
                feedbackCard.style.transition = "opacity 0.4s ease";
                feedbackCard.style.opacity = "0";

                setTimeout(() => {
                    feedbackCard.hidden = true;
                    feedbackMessage.hidden = false;
                }, 400);
            }
        } catch (error) {
            submitBtn.disabled = false;
            submitBtn.textContent = "Send Feedback";
            console.error("Feedback error:", error);
        }
    });
})();