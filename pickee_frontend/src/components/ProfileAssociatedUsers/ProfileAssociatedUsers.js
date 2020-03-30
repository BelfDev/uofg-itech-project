import ItemList from "@/components/ItemList/ItemList.vue";
import { mdiClose, mdiPlusCircle, mdiAccount, mdiMinusCircle } from '@mdi/js';
import api from "@/services/api";

export default {
    name: "ProfileAssociatedUsers",
    components: {
        ItemList
    },
    methods: {
        addAscUser: async function(e) {
            // If there is no email provided - exit
            if (this.userEmail == null) return false;

            // Register only "Enter" keydown
            if (e.type === "keydown" && e.key !== "Enter")
                return false;

            // Get user data
            const userData = await api.getUser(this.userEmail);

            // Reset the input string
            this.userEmail = '';

            if (userData.length > 0) {
                // Reset the error string
                this.errorUserLookup = '';
                const data = userData[0];
                
                // Check if the user tries to add himself/herself
                if (data.id === this.user.id) {
                    this.errorUserLookup = "You can't add yourself";
                    return false;
                }
                
                // Process the list data
                const name = (data.first_name || data.last_name) ? `${data.first_name} ${data.last_name}` : data.email;
                this.ascUsersIDs.push(data.id);
                this.ascUsersItems.push({
                    id: data.id,
                    image: data.picture,
                    text: name,
                    icon: mdiMinusCircle
                });
            } else {
                // Show the error
                this.errorUserLookup = "Sorry, we couldn't find a user with this email"
            }
        },
        removeAscUser: async function(user) {
            const targetItemIndex = this.ascUsersItems.findIndex(sourceItem => sourceItem.text === user.text);
            this.ascUsersItems.splice(targetItemIndex, 1);
            this.ascUsersIDs.splice(targetItemIndex, 1);
        },
        saveAscUsers: async function() {
            if (this.ascUsersIDs.length > 0) {
                await api.saveAscUsers(this.userID, this.ascUsersIDs);
            }
        },
    },
    mounted: async function() {
        const ascUsersResponse = await api.getAscUsers(this.userID);
        this.ascUsersItems = ascUsersResponse.map(user => {
            this.ascUsersIDs.push(user.id);
            const name = (user.first_name || user.last_name) ? `${user.first_name} ${user.last_name}` : user.email;
            return {
                id: user.id,
                image: user.picture,
                text: name,
                icon: mdiMinusCircle
            }
        });
    },
    props: ["user"],
    data: function() {
        return {
            dialog: false,
            ascUsersItems: [],
            ascUsersIDs: [],
            iconUser: mdiAccount,
            iconPlusCircle: mdiPlusCircle,
            iconClose: mdiClose,
            errorUserLookup: '',
            userEmail: null,
            userID: this.user.id
        }
    }
};
