import os
import re
import sys


def rindex(lst, value):
    return len(lst) - lst[::-1].index(value) - 1


def html_page(cls):
    def __init__(self, *args, **kwargs):
        if args:
            raise ValueError("HTML code behind class receives keyword only parameters. Positional are not allowed.")

        self.__content = None
        self.__inline_attributes = list()
        self.__inline_code_snippets = list()

        for inline_attribute in self.inline_attributes:
            if inline_attribute in dict(kwargs).keys():
                setattr(self, inline_attribute, kwargs[inline_attribute])
            else:
                setattr(self, inline_attribute, "")

    def __str__(self):
        res = self.content
        for inln in self.inline_attributes:
            res = res.replace(f"%({inln})%", getattr(self, inln))
        for cd_snpt in self.inline_code_snippets:
            res = res.replace(f"$({cd_snpt})$", eval(cd_snpt))
        return res

    @property
    def content(self):
        if not self.__content:
            fname_parts = os.path.abspath(__file__).split(os.sep)
            path_parts = fname_parts[: rindex(fname_parts, "pytest-html-reporter2") + 1]
            if sys.platform.startswith("win") or sys.platform == "cygwin":
                path_parts[0] = f"{path_parts[0]}{os.sep}"
                fname = os.path.join(*path_parts)
            else:
                fname = os.path.join(os.sep, *path_parts)
            with open(os.path.join(fname, "html", f"{cls.__doc__.strip()}.html")) as html:
                self.__content = html.read()
        return self.__content

    @property
    def inline_attributes(self):
        if not self.__inline_attributes:
            self.__inline_attributes = re.findall(r"%\((.+?)\)%", self.content)
        return self.__inline_attributes

    @property
    def inline_code_snippets(self):
        if not self.__inline_code_snippets:
            self.__inline_code_snippets = re.findall(r"\$\((.+?)\)$", self.content)
        return self.__inline_code_snippets

    def format(self, **params):
        return self.template.format(**params)

    def replace(self, one, another):
        return str(self).replace(one, another)

    cls.__init__ = __init__
    cls.__str__ = __str__
    cls.content = content
    cls.inline_attributes = inline_attributes
    cls.inline_code_snippets = inline_code_snippets
    cls.format = format
    cls.replace = replace

    return cls
