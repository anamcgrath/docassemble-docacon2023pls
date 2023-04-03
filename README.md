# docassemble.docacon2023pls

A docassemble extension.

### Install SASS compiler 

Use bootstrap example repo (https://github.com/twbs/examples/tree/main/sass-js) as a base to create sass compiler 

In terminal: 
    
    cd sass-js

    Nvm use 18

    Npm install 
  
### In scss/styles.css:

Replace components with the ones we've determined as necessary to have.

      @import "bootstrap/scss/functions"; // Required
      @import "bootstrap/scss/variables"; // Required
      @import "bootstrap/scss/mixins"; // Required
      @import "bootstrap/scss/utilities"; // added

      @import "bootstrap/scss/root"; // Required
      @import "bootstrap/scss/reboot"; // Required
      @import "bootstrap/scss/type";
      @import "bootstrap/scss/images"; // uncommented
      @import "bootstrap/scss/containers"; // added

      // @import "bootstrap/scss/code";
      @import "bootstrap/scss/grid";
      @import "bootstrap/scss/tables"; // uncommented
      @import "bootstrap/scss/forms"; // uncommented
      @import "bootstrap/scss/buttons";
      @import "bootstrap/scss/transitions";
      @import "bootstrap/scss/dropdown";
      @import "bootstrap/scss/button-group";
      // @import "bootstrap/scss/input-group"; // Requires forms
      // @import "bootstrap/scss/custom-forms";
      @import "bootstrap/scss/nav"; // uncommented
      @import "bootstrap/scss/navbar"; // Requires nav // uncommented
      // @import "bootstrap/scss/card";
      // @import "bootstrap/scss/breadcrumb";
      // @import "bootstrap/scss/pagination";
      @import "bootstrap/scss/badge"; // uncommented
      // @import "bootstrap/scss/jumbotron";
      @import "bootstrap/scss/alert"; // uncommented
      @import "bootstrap/scss/progress"; // uncommented
      // @import "bootstrap/scss/media";
      // @import "bootstrap/scss/list-group";
      @import "bootstrap/scss/close";
      @import "bootstrap/scss/toasts"; // uncommented
      @import "bootstrap/scss/modal"; // Requires transitions
      @import "bootstrap/scss/tooltip"; // uncommented
      @import "bootstrap/scss/popover"; // uncommented
      // @import "bootstrap/scss/carousel";
      @import "bootstrap/scss/spinners"; // uncommented
      // @import "bootstrap/scss/utilities";
      // @import "bootstrap/scss/print";

      // Helpers
      @import "bootstrap/scss/helpers"; // added

      // Utilities
      @import "bootstrap/scss/utilities/api"; // added

** Replace styling at bottom of scss/styles.scss: ** 
        body {
        padding: 3rem 1.5rem;
      }

      // Style Bootstrap icons
      .bi {
        fill: currentColor;
      }



