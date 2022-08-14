from datetime import date, datetime
class HouseInfo:
    def __init__(self, data):
        self.data = data

    def get_data_by_area(self, field, rec_area=0):
        # print("field is: " + field)
        # print("rec_area is: " + str(rec_area))
        field_data = []
        for record in self.data:
            # print(type(self.data))
            
            if rec_area == 0:
                field_data.append(record[field])
            elif rec_area == int(record['area']):
                field_data.append(record[field])
        return field_data              

    def get_data_by_date(self, field, rec_date=date.today()):
        field_date = []
        for record in self.data:
            if record['date'] == date.strftime(rec_date, "%m/%d/%y"):
                field_date.append(record[field])
        return field_date 