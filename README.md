# docassemble.docacon2023pls

A docassemble extension.

### Install SASS compiler 

Use bootstrap example repo (https://github.com/twbs/examples/tree/main/sass-js) as a base to create sass compiler 

In terminal: 
    
    cd sass-js

    Nvm use 18

    Npm install 
    

## CSS changes

In ``.yml`` file, link the css stylesheet to the interview:

          css: styles.css
          
 This should be below line 2 in "``features:``"
 

In ``data/static``, create a css file named "styles.css with the content: 

Like this: 


        /* @import url('./build.css'); */

        @import url('http://localhost:3000/css/styles.css'); 

In styles.css file comment @import url('./build.css');, uncomment @import url('http://localhost:3000/css/styles.css');. Change 3000 to your port if needed. It allows docassemble to include styles in development and see changes in current application immediately.

In terminal: 
        
          npm run start 


### In scss/styles.css:

Replace components with the ones we've determined as necessary to have.

        // Required
        @import "bootstrap/scss/functions";
        @import "bootstrap/scss/variables";
        @import "bootstrap/scss/maps";
        @import "bootstrap/scss/mixins";
        @import "bootstrap/scss/utilities";
        @import "bootstrap/scss/root";
        @import "bootstrap/scss/reboot";

        @import "bootstrap/scss/type";
        @import "bootstrap/scss/images"; // uncommented
        @import "bootstrap/scss/containers";
        @import "bootstrap/scss/tables"; // uncommented
        @import "bootstrap/scss/forms"; // uncommented
        @import "bootstrap/scss/buttons";
        @import "bootstrap/scss/transitions";
        @import "bootstrap/scss/dropdown";
        @import "bootstrap/scss/button-group"; // uncommented
        @import "bootstrap/scss/nav"; // uncommented
        @import "bootstrap/scss/navbar"; // Requires nav // uncommented
        // @import "bootstrap/scss/card";
        // @import "bootstrap/scss/breadcrumb";
        // @import "bootstrap/scss/accordion";
        // @import "bootstrap/scss/pagination";
        @import "bootstrap/scss/badge"; // uncommented
        @import "bootstrap/scss/alert"; // uncommented
        @import "bootstrap/scss/progress"; // uncommented
        // @import "bootstrap/scss/list-group";
        @import "bootstrap/scss/close";
        @import "bootstrap/scss/toasts"; // uncommented
        @import "bootstrap/scss/modal"; // Requires transitions
        @import "bootstrap/scss/tooltip"; // uncommented
        @import "bootstrap/scss/popover"; // uncommented
        // @import "bootstrap/scss/carousel";
        @import "bootstrap/scss/spinners"; // uncommented
        @import "bootstrap/scss/offcanvas"; // Requires transitions
        // @import "bootstrap/scss/placeholders";

        // Helpers
        @import "bootstrap/scss/helpers"; // uncommented

        // Utilities
        @import "bootstrap/scss/utilities/api";
      

### Replace styling at bottom of scss/styles.scss: 

        body {
        padding: 3rem 1.5rem;
        }

        // Style Bootstrap icons
        .bi {
        fill: currentColor;
        }
        
        

### In scss/styles.css add:

**Font Family**

At the top of the file add: 

        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=Open+Sans:wght@400;700&display=swap');
        
 Lower down in the file, add: 
 
        // Fonts
        $font-family-sans-serif: 'Open Sans', sans-serif;
        $headings-font-family: 'Montserrat';
        $headings-font-weight: 600;
        $strong-font-weight: bold;
        
        $min-contrast-ratio: 1.5;
        
 *This should be above imports*      
       

**Custom colours**

        // pls colours:
        $orange: #f3933d;
        $red: #df3644;
        $purple: #a239a6;
        $dark-blue: #267cce;
        $darker-blue: #1e63a5;
        $light-blue: #e5f1f9;
        $teal: #52bdad;
        $green: #4dab59;
        
        // Customize some defaults
        $body-color: #000;
        $body-bg: #fff;
        $border-radius: 0.4rem;
        $success: $green;

        $primary: $dark-blue;
        $secondary: $light-blue;
        $warning: $red;
        $info: $green;
        $dark: $orange;
        
  *This should be **above** imports*  
  
        
### To change logo in top left corner, add the following code to the bottom of scss/styles.css:
        
            #logo {
            background-image: url(http://localhost:3000/images/pls-logo.svg);
            display: block;
            text-indent: -9999px;
            margin: 0;
            width: 200px;
            height: 40px;
            background-size: 200px 40px;
            background-repeat: no-repeat;
        }

        @include media-breakpoint-up(sm) {
            #logo {
                width: 269px;
                height: 40px;
                background-size: 269px 40px;
            }
        }

*^Below imports*


**Add the ``svg`` logo to a folder called images in the sass compiler**


**In the .yml file, add  ``id="logo"`` to both the ``<h2/>`` and ``<h4/>`` tags**

It should now look like this: 

        logo: 
           <h2 id="logo">People's Law School</h2>
        short logo:
          <h4 id="logo">PLS</h4>
          
          

To make the change permanent, add the ``pls-logo.svg`` to ``data/static`` in this repo (docassemble-docacon2023pls).



**Change navbar colour:**

In scss/styles.css:

        #dabody .navbar.bg-light {
                background-color: $light-blue !important;
        }



### More styling changes

        // Create your own map
        $custom-colors: (
            'custom-color': #900,
        );

        // Merge the maps
        $theme-colors: map-merge($theme-colors, $custom-colors);

        .btn-warning {
            background-color: $dark-blue;
            border-color: $dark-blue;
        }
        .btn-warning:hover {
            background-color: $darker-blue;
            border-color: $dark-blue;
        }
        // checkbox subscriptions
        input.labelauty + label {
            margin-top: 0.6rem;
            margin-bottom: 0.6rem;
        }

        .navbar-brand.danavbar-title {
            overflow: visible;
        }

        .daterm {
            color: #000 !important;
            text-decoration: underline dotted rgb(75, 75, 75);
            text-underline-offset: 3px;
        }
        .daterm:hover {
            color: #000;
            text-decoration: underline dotted rgb(75, 75, 75) !important;
        }
        #daattributions {
            margin-top: 18px;
        }

        .required-explain {
            color: $warning;
            font-size: 12px;
        }

        .da-form-group.row.da-field-container.da-field-container-note {
            margin-top: -0.7rem;
            margin-bottom: -0.2rem !important;
            font-size: 12px;
            opacity: 65%;
        }

        .dafooter {
            opacity: 70%;
            font-size: 12px;
            text-align: center;
            line-height: 18px !important;
        }
        footer.bg-light.dafooter {
            background-color: #fff !important;
        }


## To put these changes in the ``data/static/build.css`` file 

In terminal: 

      npm run build
      
Copy content of ``css/styles.css`` to ``data/static/build.css`` in your docassemble repo

In ``data/static``, create another css file named "styles.css with the content: 

           @import url('./build.css');

        /* @import url('http://localhost:3000/css/styles.css'); */
