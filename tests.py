import unittest
from main import search_img_links


class LookingForSrcTestCase(unittest.TestCase):
    def add_to_list(self, re_obj):
        l = [i.group(1) for i in re_obj]
        return l

    def test_1(self):
        test_string1 = '<div role="button" tabindex="0" class="ij ik di il bf im"><div class="er es ie"><picture><source srcset="https://miro.medium.com/v2/resize:fit:640/format:webp/1*qqA5qTzBqgmoPMrSk6Ho8A.png 640w, https://miro.medium.com/v2/resize:fit:720/format:webp/1*qqA5qTzBqgmoPMrSk6Ho8A.png 720w, https://miro.medium.com/v2/resize:fit:750/format:webp/1*qqA5qTzBqgmoPMrSk6Ho8A.png 750w, https://miro.medium.com/v2/resize:fit:786/format:webp/1*qqA5qTzBqgmoPMrSk6Ho8A.png 786w, https://miro.medium.com/v2/resize:fit:828/format:webp/1*qqA5qTzBqgmoPMrSk6Ho8A.png 828w, https://miro.medium.com/v2/resize:fit:1100/format:webp/1*qqA5qTzBqgmoPMrSk6Ho8A.png 1100w, https://miro.medium.com/v2/resize:fit:1400/format:webp/1*qqA5qTzBqgmoPMrSk6Ho8A.png 1400w" sizes="(min-resolution: 4dppx) and (max-width: 700px) 50vw, (-webkit-min-device-pixel-ratio: 4) and (max-width: 700px) 50vw, (min-resolution: 3dppx) and (max-width: 700px) 67vw, (-webkit-min-device-pixel-ratio: 3) and (max-width: 700px) 65vw, (min-resolution: 2.5dppx) and (max-width: 700px) 80vw, (-webkit-min-device-pixel-ratio: 2.5) and (max-width: 700px) 80vw, (min-resolution: 2dppx) and (max-width: 700px) 100vw, (-webkit-min-device-pixel-ratio: 2) and (max-width: 700px) 100vw, 700px" type="image/webp"><source data-testid="og" srcset="https://miro.medium.com/v2/resize:fit:640/1*qqA5qTzBqgmoPMrSk6Ho8A.png 640w, https://miro.medium.com/v2/resize:fit:720/1*qqA5qTzBqgmoPMrSk6Ho8A.png 720w, https://miro.medium.com/v2/resize:fit:750/1*qqA5qTzBqgmoPMrSk6Ho8A.png 750w, https://miro.medium.com/v2/resize:fit:786/1*qqA5qTzBqgmoPMrSk6Ho8A.png 786w, https://miro.medium.com/v2/resize:fit:828/1*qqA5qTzBqgmoPMrSk6Ho8A.png 828w, https://miro.medium.com/v2/resize:fit:1100/1*qqA5qTzBqgmoPMrSk6Ho8A.png 1100w, https://miro.medium.com/v2/resize:fit:1400/1*qqA5qTzBqgmoPMrSk6Ho8A.png 1400w" sizes="(min-resolution: 4dppx) and (max-width: 700px) 50vw, (-webkit-min-device-pixel-ratio: 4) and (max-width: 700px) 50vw, (min-resolution: 3dppx) and (max-width: 700px) 67vw, (-webkit-min-device-pixel-ratio: 3) and (max-width: 700px) 65vw, (min-resolution: 2.5dppx) and (max-width: 700px) 80vw, (-webkit-min-device-pixel-ratio: 2.5) and (max-width: 700px) 80vw, (min-resolution: 2dppx) and (max-width: 700px) 100vw, (-webkit-min-device-pixel-ratio: 2) and (max-width: 700px) 100vw, 700px"><img alt="" class="bf in io c" width="700" height="394" loading="eager" role="presentation" src="https://miro.medium.com/v2/resize:fit:1400/1*qqA5qTzBqgmoPMrSk6Ho8A.png"></picture></div></div>'
        res = self.add_to_list(search_img_links(test_string1))
        self.assertEqual(res, ['https://miro.medium.com/v2/resize:fit:1400/1*qqA5qTzBqgmoPMrSk6Ho8A.png'])

    def test_2(self):
        test_string2 = '''<p>
            <img decoding="async" class="alignnone
                wp-image-166540 size-full lazy entered loaded" src="https://media.tproger.ru/uploads/2021/01/3-9.jpg"
                alt="Синтаксис regex" width="662" height="474" data-src="https://media.tproger.ru/uploads/2021/01/3-9.jpg"
                >
            </p>'''
        res = self.add_to_list(search_img_links(test_string2))
        self.assertEqual(res, ['https://media.tproger.ru/uploads/2021/01/3-9.jpg'])

    def test_3(self):
        test_string3 = '<img >'
        res = self.add_to_list(search_img_links(test_string3))
        self.assertEqual(res, [])

    def test_4(self):
        test_string4 = '<img class="img_boot" src="/auto.png"> <img id="ffr" style="color:red" src="bicycle.png">'
        res = self.add_to_list(search_img_links(test_string4))
        self.assertEqual(res, ['/auto.png', 'bicycle.png'])

    def test_5(self):
        test_string5 = '<div class="swiper-slide swiper-slide-next" style="margin-right: 20px;"><div class="tm-stories-card"><button class="tm-stories-card__image-block"><img alt="" src="https://habrastorage.org/r/w390/getpro/habr/upload_files/500/416/672/500416672540bb5785f750f03cfaebcc.png" class="tm-stories-card__image"> <div class="tm-stories-card__gradient"></div> <!----> <a href="https://u.habr.com/on6br" class="tm-stories-card__author"><img alt="author-logo" src="https://habrastorage.org/getpro/habr/upload_files/086/89e/632/08689e632aca9e7a8b3ce0cbf90684ad.png" class="tm-stories-card__author-logo"></a></button> <div class="tm-stories-card__title">Активность найма на IT-рынке в марте</div></div></div>'
        res = self.add_to_list(search_img_links(test_string5))
        self.assertEqual(res,
            ['https://habrastorage.org/r/w390/getpro/habr/upload_files/500/416/672/500416672540bb5785f750f03cfaebcc.png',
            'https://habrastorage.org/getpro/habr/upload_files/086/89e/632/08689e632aca9e7a8b3ce0cbf90684ad.png'])

    def test_6(self):
        test_string6 = '<button class="tm-stories-card__image-block"><img alt="" src="https://habrastorage.org/r/w390/getpro/habr/upload_files/ab0/bb6/c7c/ab0bb6c7c353925f61448eb7beec4bc6.jpg" class="tm-stories-card__image"> <div class="tm-stories-card__gradient"></div> <!----> <a href="https://u.habr.com/1zgg0" class="tm-stories-card__author"><img alt="author-logo" src="https://habrastorage.org/getpro/habr/upload_files/b8a/c91/391/b8ac9139163036dcfc8b7cb45c71f057.png" class="tm-stories-card__author-logo"></a></button>'
        res = self.add_to_list(search_img_links(test_string6))
        self.assertEqual(res,
            ['https://habrastorage.org/r/w390/getpro/habr/upload_files/ab0/bb6/c7c/ab0bb6c7c353925f61448eb7beec4bc6.jpg',
             'https://habrastorage.org/getpro/habr/upload_files/b8a/c91/391/b8ac9139163036dcfc8b7cb45c71f057.png'])

    def test_7(self):
        test_string7 = '<div role="button" tabindex="0" class="ij ik di il bf im"><div class="er es ie"><picture><source srcset="https://miro.medium.com/v2/resize:fit:640/format:webp/1*qqA5qTzBqgmoPMrSk6Ho8A.png 640w, https://miro.medium.com/v2/resize:fit:720/format:webp/1*qqA5qTzBqgmoPMrSk6Ho8A.png 720w, https://miro.medium.com/v2/resize:fit:750/format:webp/1*qqA5qTzBqgmoPMrSk6Ho8A.png 750w, https://miro.medium.com/v2/resize:fit:786/format:webp/1*qqA5qTzBqgmoPMrSk6Ho8A.png 786w, https://miro.medium.com/v2/resize:fit:828/format:webp/1*qqA5qTzBqgmoPMrSk6Ho8A.png 828w, https://miro.medium.com/v2/resize:fit:1100/format:webp/1*qqA5qTzBqgmoPMrSk6Ho8A.png 1100w, https://miro.medium.com/v2/resize:fit:1400/format:webp/1*qqA5qTzBqgmoPMrSk6Ho8A.png 1400w" sizes="(min-resolution: 4dppx) and (max-width: 700px) 50vw, (-webkit-min-device-pixel-ratio: 4) and (max-width: 700px) 50vw, (min-resolution: 3dppx) and (max-width: 700px) 67vw, (-webkit-min-device-pixel-ratio: 3) and (max-width: 700px) 65vw, (min-resolution: 2.5dppx) and (max-width: 700px) 80vw, (-webkit-min-device-pixel-ratio: 2.5) and (max-width: 700px) 80vw, (min-resolution: 2dppx) and (max-width: 700px) 100vw, (-webkit-min-device-pixel-ratio: 2) and (max-width: 700px) 100vw, 700px" type="image/webp"><source data-testid="og" srcset="https://miro.medium.com/v2/resize:fit:640/1*qqA5qTzBqgmoPMrSk6Ho8A.png 640w, https://miro.medium.com/v2/resize:fit:720/1*qqA5qTzBqgmoPMrSk6Ho8A.png 720w, https://miro.medium.com/v2/resize:fit:750/1*qqA5qTzBqgmoPMrSk6Ho8A.png 750w, https://miro.medium.com/v2/resize:fit:786/1*qqA5qTzBqgmoPMrSk6Ho8A.png 786w, https://miro.medium.com/v2/resize:fit:828/1*qqA5qTzBqgmoPMrSk6Ho8A.png 828w, https://miro.medium.com/v2/resize:fit:1100/1*qqA5qTzBqgmoPMrSk6Ho8A.png 1100w, https://miro.medium.com/v2/resize:fit:1400/1*qqA5qTzBqgmoPMrSk6Ho8A.png 1400w" sizes="(min-resolution: 4dppx) and (max-width: 700px) 50vw, (-webkit-min-device-pixel-ratio: 4) and (max-width: 700px) 50vw, (min-resolution: 3dppx) and (max-width: 700px) 67vw, (-webkit-min-device-pixel-ratio: 3) and (max-width: 700px) 65vw, (min-resolution: 2.5dppx) and (max-width: 700px) 80vw, (-webkit-min-device-pixel-ratio: 2.5) and (max-width: 700px) 80vw, (min-resolution: 2dppx) and (max-width: 700px) 100vw, (-webkit-min-device-pixel-ratio: 2) and (max-width: 700px) 100vw, 700px"><img alt="" class="bf in io c" width="700" height="394" loading="eager" role="presentation" src="https://miro.medium.com/v2/resize:fit:1400/1*qqA5qTzBqgmoPMrSk6Ho8A.png"></picture></div></div>'
        res = self.add_to_list(search_img_links(test_string7))
        self.assertEqual(res, ['https://miro.medium.com/v2/resize:fit:1400/1*qqA5qTzBqgmoPMrSk6Ho8A.png'])

    def test_8(self):
        test_string8 = '<img alt="" src="https://habrastorage.org/r/w390/getpro/habr/upload_files/c3c/f8f/3f4/c3cf8f3f470787454666ed3e94ab58ef.png" class="tm-stories-card__image">'
        res = self.add_to_list(search_img_links(test_string8))
        self.assertEqual(res, ['https://habrastorage.org/r/w390/getpro/habr/upload_files/c3c/f8f/3f4/c3cf8f3f470787454666ed3e94ab58ef.png'])

    def test_9(self):
        test_string9 = '<div class="v4d862463"><div data-name="adaptiveImageTransform" class="qe11b95f bd1194143"><img data-name="adaptiveImage" src="https://avatars.mds.yandex.net/get-direct/5275446/9YnFFSPy5loxR8OazKcayQ/x450" elementtiming="tgo-ssr-image" class="c11f06b17"></div></div>'
        res = self.add_to_list(search_img_links(test_string9))
        self.assertEqual(res, ['https://avatars.mds.yandex.net/get-direct/5275446/9YnFFSPy5loxR8OazKcayQ/x450'])

    def test_10(self):
        test_string10 = '<div data-name="adaptiveImageContainer" data-x="0.5246913580246914" data-y="0.6361111111111111" data-width="162" data-height="180" data-cropped-width="154" data-cropped-height="119" class="rdd0ad337 i4396e6e7"><div class="v4d862463"><div data-name="adaptiveImageTransform" class="qe11b95f x88263e20"><img data-name="adaptiveImage" src="https://avatars.mds.yandex.net/get-direct/4248063/eU9YmqFMglpOOS0xEu_D8g/y180" elementtiming="tgo-ssr-image" class="c11f06b17"></div></div></div>'
        res = self.add_to_list(search_img_links(test_string10))
        self.assertEqual(res, ['https://avatars.mds.yandex.net/get-direct/4248063/eU9YmqFMglpOOS0xEu_D8g/y180'])

    def test_11(self):
        test_string11 = '<img src="pic5.jpg">'
        res = self.add_to_list(search_img_links(test_string11))
        self.assertEqual(res, ['pic5.jpg'])


