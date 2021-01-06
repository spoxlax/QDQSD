class resolver():
    def __init__(self,email):
        domain_remover = email.split('@')
        # print(domain_remover)
        clean_name = domain_remover[0].split('.')
        # print(clean_name)
        if 'ext' in clean_name:
            if len(clean_name) == 3:
                self.first_name = clean_name[0]
                self.last_name = clean_name[1]
        else:
            if len(clean_name) == 4:
                self.first_name = clean_name[0] + ' ' + clean_name[1]
                self.last_name = clean_name[2] + ' ' + clean_name[3]
            elif len(clean_name) == 3:
                self.first_name = clean_name[0] + ' ' + clean_name[1]
                self.last_name = clean_name[2]
            elif len(clean_name) == 1:
                self.first_name = clean_name[0]
                self.last_name = None
            else:
                self.first_name = clean_name[0]
                self.last_name = clean_name[1]
