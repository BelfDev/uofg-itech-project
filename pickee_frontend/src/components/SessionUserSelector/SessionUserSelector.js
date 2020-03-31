import ItemList from "@/components/ItemList/ItemList.vue";
import { mdiPlusCircle, mdiPlus, mdiClose, mdiMinusCircle, mdiAccount } from '@mdi/js';
import api from "@/services/api";

export default {
    name: "SessionUserSelector",
    components: {
        ItemList
    },
    methods: {
        removeSessionUser: function(sessionUser) {
            this.associatedUsers.find(ascUser => sessionUser.id === ascUser.id).hidden = false;
            const userIndex = this.selectedUsers.findIndex(sourceItem => sourceItem.id === sessionUser.id);
            this.selectedUsers.splice(userIndex, 1);
        },
        selectSessionUser: function(sessionUser) {
            this.associatedUsers.find(ascUser => sessionUser.id === ascUser.id).hidden = true;
            this.selectedUsers.push({
                id: sessionUser.id,
                image: sessionUser.picture,
                text: sessionUser.text,
                icon: mdiMinusCircle,
                type: 'person'
            });
        },
        addSessionUser: async function(e) {
            // If there is no email - exit
            if (this.userEmail == null) return false;

            // Allow only enter keyword
            if (e.type === "keydown" && e.key !== "Enter")
                return false;

            const userData = await api.getUser(this.userEmail);

            // Reset the input value
            this.userEmail = '';

            if (userData.length > 0) {
                // Reset the error
                this.errorUserLookup = '';
                const data = userData[0];
                
                // Check if the user is trying to add himself/herself
                if (data.id === this.user.id) {
                    this.errorUserLookup = "Your preferences are already considered";
                    return false;
                }
                
                // Find if it's an associated user
                const ascUser = this.associatedUsers.find(user => data.id === user.id);
                if (ascUser) ascUser.hidden = true;

                // Process the list data
                const name = (data.first_name || data.last_name) ? `${data.first_name} ${data.last_name}` : data.email;
                this.selectedUsers.push({
                    id: data.id,
                    image: data.picture,
                    text: name,
                    icon: mdiMinusCircle,
                    type: 'person'
                });
            } else {
                // Show the error
                this.errorUserLookup = "Sorry, we couldn't find a user with this email"
            }
        }
    },
    mounted: async function() {
        // Populate the list of associated users
        if (this.user && this.user.id) {
            const ascUsersResponse = await api.getAscUsers(this.user.id);
            ascUsersResponse.map(user => {
                const name = (user.first_name || user.last_name) ? `${user.first_name} ${user.last_name}` : user.email;
                this.associatedUsers.push({
                    id: user.id,
                    image: user.picture,
                    text: name,
                    icon: mdiPlusCircle,
                    type: 'person',
                    hidden: false
                });
            });
        }
    },
    computed: {
        displayedAssociatedUsers: function() {
            return this.associatedUsers.filter(user => user.hidden === false)
        },
        userIDs: function() {
            return this.selectedUsers.map(item => item.id).join(',');
        }
    },
    props: ['user', 'urls'],
    data: () => ({
        selectedUsers: [],
        associatedUsers: [],
        iconUser: mdiAccount,
        iconPlusCircle: mdiPlusCircle,
        iconPlus: mdiPlus,
        iconClose: mdiClose,
        errorUserLookup: '',
        userEmail: null,
        dialog: false,
    })
}