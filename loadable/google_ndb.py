from fixture.loadable.google_datastore_loadable import GoogleDatastoreFixture, EntityMedium

class NdbEntityMedium(EntityMedium):
            
    def clear(self, obj):
        """Delete this entity from the Datastore"""
        obj.key.delete()
    
class NdbDatastoreFixture(GoogleDatastoreFixture):
    Medium = NdbEntityMedium
    
        