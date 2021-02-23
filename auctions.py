class Auction:

    def __init__(self, ID, model, gigs, grade, count, price, listing):
        self.ID = ID
        self.model = model
        self.gig = gigs
        self.grade = grade
        self.count = count
        self.price = price
        self.link = listing

    def specs(self):
        return (
                    self.ID + ', ' + self.model + ', ' + self.gig + ', ' + self.grade + ', ' + self.count + ', ' + self.price + ', ' + self.link)


class SupAuction:
    def __init__(self, startIndex, manifest, ID='No ID', price='No price', listing='No link'):
        self.ID = ID
        try:
            self.make = manifest[startIndex].split()[1]
        except:
            self.make = manifest[startIndex].split()[0]
        self.model = manifest[startIndex+1]
        self.grade = manifest[startIndex+2]
        self.count = manifest[startIndex+3]
        self.description = manifest[startIndex+4]
        self.category = manifest[startIndex+5]
        self.network = manifest[startIndex+6]
        self.fID = manifest[startIndex+7]
        self.fName = manifest[startIndex+8]
        self.currency = manifest[startIndex+9]
        try:
            if manifest[startIndex+10].split()[0][0:1].isdigit():
                self.capacity = manifest[startIndex+10].split()[0]
            else:
                self.capacity = ''
        except:
            self.capacity = ''
        self.price = price
        self.link = listing

    def specs(self):
        return(self.ID+', '+self.make+', '+self.model+', '+self.grade+', '+self.count+', '+str(self.price)+', '+self.description+','
               + self.category+', '+self.network+', '+self.fID+', '+self.fName+', '+self.currency+', '+self.capacity+', '+self.link)


class SelectAuction:
    def __init__(self, startIndex, manifest, ID='No ID', price='No price', listing='No link'):
        self.ID = ID
        self.price = price
        self.link = listing

        self.make = manifest[startIndex + 1]
        self.model = manifest[startIndex + 2]
        self.network = manifest[startIndex + 3]
        self.capacity = manifest[startIndex + 4]
        self.grade = manifest[startIndex + 5]
        self.count = manifest[startIndex + 6]
        self.description = manifest[startIndex + 7]

    def specs(self):
        return (self.ID + ', ' + self.make + ', ' + self.model + ', ' + self.grade + ', ' + self.count + ', ' + str(
            self.price) + ', ' + self.description + ', ' + self.network + ', ' + self.capacity + ', ' + self.link)