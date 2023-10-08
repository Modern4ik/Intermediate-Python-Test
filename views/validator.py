class Validator:
    @classmethod
    def validate_data(cls, user_data):
        if not (len(user_data[0]) == 0 or len(user_data[1]) == 0):
            return False

        return True
    
    @classmethod
    def validate_id(cls, user_id: str):
        if user_id.isdigit():
            return False
        
        return True
