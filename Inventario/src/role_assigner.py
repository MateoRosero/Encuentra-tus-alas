class RoleAssigner:
    @staticmethod
    def assign_role(email):
        if email.endswith('@aerolinea.com'):
            return 'airline'
        elif email.endswith('@admin.com'):
            return 'admin'
        else:
            return 'passenger'
