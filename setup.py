import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.docacon2023pls',
      version='0.0.2',
      description=('A docassemble extension.'),
      long_description='# docassemble.docacon2023pls\r\n\r\nA docassemble extension.\r\n\r\n### Install SASS compiler \r\n\r\nUse bootstrap example repo (https://github.com/twbs/examples/tree/main/sass-js) as a base to create sass compiler \r\n\r\nIn terminal: \r\n    \r\n    cd sass-js\r\n\r\n    Nvm use 18\r\n\r\n    Npm install \r\n    \r\n\r\n## CSS changes\r\n\r\nIn ``.yml`` file, link the css stylesheet to the interview:\r\n\r\n          css: styles.css\r\n          \r\n This should be below line 2 in "``features:``"\r\n \r\n\r\nIn ``data/static``, create a css file named "styles.css with the content: \r\n\r\nLike this: \r\n\r\n\r\n        /* @import url(\'./build.css\'); */\r\n\r\n        @import url(\'http://localhost:3000/css/styles.css\'); \r\n\r\nIn styles.css file comment @import url(\'./build.css\');, uncomment @import url(\'http://localhost:3000/css/styles.css\');. Change 3000 to your port if needed. It allows docassemble to include styles in development and see changes in current application immediately.\r\n\r\nIn terminal: \r\n        \r\n          npm run start \r\n\r\n\r\n### In scss/styles.css:\r\n\r\nReplace components with the ones we\'ve determined as necessary to have.\r\n\r\n        // Required\r\n        @import "bootstrap/scss/functions";\r\n        @import "bootstrap/scss/variables";\r\n        @import "bootstrap/scss/maps";\r\n        @import "bootstrap/scss/mixins";\r\n        @import "bootstrap/scss/utilities";\r\n        @import "bootstrap/scss/root";\r\n        @import "bootstrap/scss/reboot";\r\n\r\n        @import "bootstrap/scss/type";\r\n        @import "bootstrap/scss/images"; // uncommented\r\n        @import "bootstrap/scss/containers";\r\n        @import "bootstrap/scss/tables"; // uncommented\r\n        @import "bootstrap/scss/forms"; // uncommented\r\n        @import "bootstrap/scss/buttons";\r\n        @import "bootstrap/scss/transitions";\r\n        @import "bootstrap/scss/dropdown";\r\n        @import "bootstrap/scss/button-group"; // uncommented\r\n        @import "bootstrap/scss/nav"; // uncommented\r\n        @import "bootstrap/scss/navbar"; // Requires nav // uncommented\r\n        // @import "bootstrap/scss/card";\r\n        // @import "bootstrap/scss/breadcrumb";\r\n        // @import "bootstrap/scss/accordion";\r\n        // @import "bootstrap/scss/pagination";\r\n        @import "bootstrap/scss/badge"; // uncommented\r\n        @import "bootstrap/scss/alert"; // uncommented\r\n        @import "bootstrap/scss/progress"; // uncommented\r\n        // @import "bootstrap/scss/list-group";\r\n        @import "bootstrap/scss/close";\r\n        @import "bootstrap/scss/toasts"; // uncommented\r\n        @import "bootstrap/scss/modal"; // Requires transitions\r\n        @import "bootstrap/scss/tooltip"; // uncommented\r\n        @import "bootstrap/scss/popover"; // uncommented\r\n        // @import "bootstrap/scss/carousel";\r\n        @import "bootstrap/scss/spinners"; // uncommented\r\n        @import "bootstrap/scss/offcanvas"; // Requires transitions\r\n        // @import "bootstrap/scss/placeholders";\r\n\r\n        // Helpers\r\n        @import "bootstrap/scss/helpers"; // uncommented\r\n\r\n        // Utilities\r\n        @import "bootstrap/scss/utilities/api";\r\n      \r\n\r\n### Replace styling at bottom of scss/styles.scss: \r\n\r\n        body {\r\n        padding: 3rem 1.5rem;\r\n        }\r\n\r\n        // Style Bootstrap icons\r\n        .bi {\r\n        fill: currentColor;\r\n        }\r\n        \r\n        \r\n\r\n### In scss/styles.css add:\r\n\r\n**Font Family**\r\n\r\nAt the top of the file add: \r\n\r\n        @import url(\'https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=Open+Sans:wght@400;700&display=swap\');\r\n        \r\n Lower down in the file, add: \r\n \r\n        // Fonts\r\n        $font-family-sans-serif: \'Open Sans\', sans-serif;\r\n        $headings-font-family: \'Montserrat\';\r\n        $headings-font-weight: 600;\r\n        $strong-font-weight: bold;\r\n\r\n**Custom colours**\r\n\r\n        // pls colours:\r\n        $orange: #f3933d;\r\n        $red: #df3644;\r\n        $purple: #a239a6;\r\n        $dark-blue: #267cce;\r\n        $darker-blue: #1e63a5;\r\n        $light-blue: #e5f1f9;\r\n        $teal: #52bdad;\r\n        $green: #4dab59;\r\n        \r\n        // Customize some defaults\r\n        $body-color: #000;\r\n        $body-bg: #fff;\r\n        $border-radius: 0.4rem;\r\n        $success: $green;\r\n\r\n        $primary: $dark-blue;\r\n        $secondary: $light-blue;\r\n        $warning: $red;\r\n        $info: $green;\r\n        $dark: $orange;\r\n        \r\n       \r\n        \r\n### To change logo in top left corner, add the following code to the bottom of scss/styles.css:\r\n        \r\n            #logo {\r\n            background-image: url(http://localhost:3000/images/pls-logo.svg);\r\n            display: block;\r\n            text-indent: -9999px;\r\n            margin: 0;\r\n            width: 200px;\r\n            height: 40px;\r\n            background-size: 200px 40px;\r\n            background-repeat: no-repeat;\r\n        }\r\n\r\n        @include media-breakpoint-up(sm) {\r\n            #logo {\r\n                width: 269px;\r\n                height: 40px;\r\n                background-size: 269px 40px;\r\n            }\r\n        }\r\n\r\n\r\n**Add the ``svg`` logo to a folder called images in the sass compiler**\r\n\r\n\r\n**In the .yml file, add  ``id="logo"`` to both the ``<h2/>`` and ``<h4/>`` tags**\r\n\r\nIt should now look like this: \r\n\r\n        logo: \r\n           <h2 id="logo">People\'s Law School</h2>\r\n        short logo:\r\n          <h4 id="logo">PLS</h4>\r\n          \r\n          \r\n\r\nTo make the change permanent, add the ``pls-logo.svg`` to ``data/static`` in this repo (docassemble-docacon2023pls).\r\n\r\n\r\n\r\n**Change navbar colour:**\r\n\r\nIn scss/styles.css:\r\n\r\n        #dabody .navbar.bg-light {\r\n                background-color: $light-blue !important;\r\n        }\r\n\r\n\r\n\r\n### More styling changes\r\n\r\n        // Create your own map\r\n        $custom-colors: (\r\n            \'custom-color\': #900,\r\n        );\r\n\r\n        // Merge the maps\r\n        $theme-colors: map-merge($theme-colors, $custom-colors);\r\n\r\n        .btn-warning {\r\n            background-color: $dark-blue;\r\n            border-color: $dark-blue;\r\n        }\r\n        .btn-warning:hover {\r\n            background-color: $darker-blue;\r\n            border-color: $dark-blue;\r\n        }\r\n        // checkbox subscriptions\r\n        input.labelauty + label {\r\n            margin-top: 0.6rem;\r\n            margin-bottom: 0.6rem;\r\n        }\r\n\r\n        .navbar-brand.danavbar-title {\r\n            overflow: visible;\r\n        }\r\n\r\n        .daterm {\r\n            color: #000 !important;\r\n            text-decoration: underline dotted rgb(75, 75, 75);\r\n            text-underline-offset: 3px;\r\n        }\r\n        .daterm:hover {\r\n            color: #000;\r\n            text-decoration: underline dotted rgb(75, 75, 75) !important;\r\n        }\r\n        #daattributions {\r\n            margin-top: 18px;\r\n        }\r\n\r\n        .required-explain {\r\n            color: $warning;\r\n            font-size: 12px;\r\n        }\r\n\r\n        .da-form-group.row.da-field-container.da-field-container-note {\r\n            margin-top: -0.7rem;\r\n            margin-bottom: -0.2rem !important;\r\n            font-size: 12px;\r\n            opacity: 65%;\r\n        }\r\n\r\n        .dafooter {\r\n            opacity: 70%;\r\n            font-size: 12px;\r\n            text-align: center;\r\n            line-height: 18px !important;\r\n        }\r\n        footer.bg-light.dafooter {\r\n            background-color: #fff !important;\r\n        }\r\n\r\n\r\n## To put these changes in the ``data/static/build.css`` file \r\n\r\nIn terminal: \r\n\r\n      npm run build\r\n      \r\nCopy content of ``css/styles.css`` to ``data/static/build.css`` in your docassemble repo\r\n\r\nIn ``data/static``, create another css file named "styles.css with the content: \r\n\r\n           @import url(\'./build.css\');\r\n\r\n        /* @import url(\'http://localhost:3000/css/styles.css\'); */\r\n',
      long_description_content_type='text/markdown',
      author='Ana McGrath',
      author_email='mcgrathana@gmail.com',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/docacon2023pls/', package='docassemble.docacon2023pls'),
     )

