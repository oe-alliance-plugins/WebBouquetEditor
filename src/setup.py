from setuptools import setup
import setup_translate

pkg = 'Extensions.WebBouquetEditor'
setup(name='enigma2-plugin-extensions-webbouqueteditor',
       version='3.0',
       description='Extension for enigma2 webinterface to sort bouquets and other',
       package_dir={pkg: 'WebBouquetEditor'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'LICENSE', 'maintainer.info', 'web/*.xml', 'web-data/*.js', 'web-data/*.htm', 'web-data/*.html', 'web-data/*.gif', 'web-data/*.png', 'web-data/*.css']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
