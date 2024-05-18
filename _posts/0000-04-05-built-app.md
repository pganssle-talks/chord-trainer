<div class="fragment disappearing-fragment fade-out" data-fragment-index="0">
    <img src="images/vxxx-red-yellow.png"
         class="screenshot splash"
         style="height: 75dvh"
         alt="A screenshot of a simple website with a dark background and two
              colored rectangles — a red one on the left and a yellow on the right.
              Beneath it is text that says 0/0 and a pulldown that says 'Yellow (CFA)'"
              />
</div>

<div class="fragment disappearing-fragment fade-in-and-out" data-fragment-index="0">
    <img src="images/vxxx-red-yellow-right.png"
         class="screenshot splash"
         style="height: 75dvh"
         alt="A screenshot of a simple website with a dark background and two
              colored rectangles — a red one on the left and a yellow on the right.
              Beneath it is text that says 0/0 and a pulldown that says 'Yellow (CFA)'"
              />
</div>

<div class="fragment disappearing-fragment fade-in-and-out" data-fragment-index="1">
    <img src="images/vxxx-red-yellow-wrong.png"
         class="screenshot splash"
         style="height: 75dvh"
         alt="A screenshot of a simple website with a dark background and two
              colored rectangles — a red one on the left and a yellow on the right.
              Beneath it is text that says 0/0 and a pulldown that says 'Yellow (CFA)'"
              />
</div>

<div class="fragment disappearing-fragment fade-in-and-out" data-fragment-index="2">
    <img src="images/vxxx-green.png"
         class="screenshot splash"
         style="height: 75dvh"
         alt="A screenshot of a simple website with a dark background and two
              colored rectangles — a red one on the left and a yellow on the right.
              Beneath it is text that says 0/0 and a pulldown that says 'Yellow (CFA)'"
              />
</div>

<div class="fragment disappearing-fragment fade-in" data-fragment-index="3">
    <img src="images/vxxx-gray.png"
         class="screenshot splash"
         style="height: 75dvh"
         alt="At the gray chord"
              />
</div>

<div class="fragment disappearing-fragment fade-in" data-fragment-index="4">
    <img src="images/vxxx-manual-player.png"
         class="screenshot splash"
         style="height: 75dvh"
         alt="A screenshot of a simple website with a dark background and two
              colored rectangles — a red one on the left and a yellow on the right.
              Beneath it is text that says 0/0 and a pulldown that says 'Yellow (CFA)'"
              />
</div>

Notes:

No, of course we're not going to do any of that — this kind of thing is exactly what being a programmer is all about! So obviously I built an app!

I threw together a quick HTML / Javascript / CSS single-page app, permissively-licensed open source, and published via github pages.

Here is what it looks like, it's pretty simple: it displays the chords you are on, it will play one randomly, and you pick which one you think it is. If you get it right, the kitty is happy. If you get it wrong, the kitty is sad.

When the child starts mastering chords. you can move on to the next level. There are 9 "white key" chords, and once they master all of those, you enter the "black key" phase, where they're supposed to start calling out the chords by name rather than color.

--

<video src="videos/cim_how_to_clip.webm"
       style="height: 70dvh"
       controls type="video/webm">

Notes:

So, let's see it in action!

--

<!-- .slide: data-visibility="hidden" -->

<div style="display: flex; flex-direction: rows; align-items: center; justify-content:space-around; height: 80dvh">
<img src="images/pwa-install-app.png" style="max-height:100%; max-width: 30dvh">
<img src="images/pwa-install-installing.png" style="max-height:100%; max-width: 30dvh">
<img src="images/pwa-install-icon.png" style="max-height:100%; max-width: 40dvh">

Notes:

Additionally, I found out that when you have a simple single page application like this, it's fairly easy to turn it into a "progressive web app", so actually if you open it on your phone or tablet in a browser, you can click "install this app", and it will actually install it like a native application.

