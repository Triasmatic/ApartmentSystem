class tenantList:

    def __init__(self):
        self.tenants = []

    def insertTenant(self, tenant):
        self.tenants.append(tenant)

    def getAptNumber(self, string):
        pass

    def display(self):
        for t in self.tenants:
            print(f"Tenant: {t.getName}, Apt Number: {t.getAptNumber}")