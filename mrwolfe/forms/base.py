class PartialUpdateMixin(object):

    def update(self, commit=True):

        """ Allow for updates of only the fields available in the form """

        for f in self.instance._meta.fields:
            if f.attname in self.fields:
                setattr(self.instance, f.attname,
                        self.cleaned_data[f.attname])
        if commit:
            try:
                self.instance.save()
            except:
                return False

        return self.instance
