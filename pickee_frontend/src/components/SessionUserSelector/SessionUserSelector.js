import ItemList from "@/components/ItemList/ItemList.vue";
import { mdiPlusCircle, mdiPlus, mdiClose, mdiMinusCircle, mdiAccount } from '@mdi/js';
import api from "@/services/api";

export default {
    name: "SessionUserSelector",
    components: {
        ItemList
    },
    methods: {
        removeFriend: function(friend) {
            this.associatedFriends.find(ascFriend => friend.id === ascFriend.id).hidden = false;
            const friendIndex = this.selectedFriends.findIndex(sourceItem => sourceItem.id === friend.id);
            this.selectedFriends.splice(friendIndex, 1);
        },
        selectFriend: function(friend) {
            this.associatedFriends.find(ascFriend => friend.id === ascFriend.id).hidden = true;
            this.selectedFriends.push({
                id: friend.id,
                image: friend.picture,
                text: friend.text,
                icon: mdiMinusCircle
            });
        },
        addFriend: async function(e) {
            if (this.friendEmail == null) return false;
            if (e.type === "keydown" && e.key !== "Enter")
                return false;

            const friendData = await api.getFriend(this.friendEmail);
            this.friendEmail = '';

            if (friendData.length > 0) {
                this.errorFriendLookup = null;
                const data = friendData[0];
                
                if (data.id === this.user.id) {
                    this.errorFriendLookup = "Your preferences are already considered";
                    return false;
                }
                
                const ascFriend = this.associatedFriends.find(ascFriend => data.id === ascFriend.id);
                if (ascFriend) ascFriend.hidden = true;

                const name = (data.first_name || data.last_name) ? `${data.first_name} ${data.last_name}` : data.email;
                this.selectedFriends.push({
                    id: data.id,
                    image: data.picture,
                    text: name,
                    icon: mdiMinusCircle
                });
                this.userIDs = this.selectedFriends.map(item => item.id).join(',');
            } else {
                this.errorFriendLookup = "Sorry, we couldn't find a user with this email"
            }
        }
    },
    mounted: async function() {
        const friendsResponse = await api.getFriends(this.user.id);
        this.friendsItems = friendsResponse.map(friend => {
            this.associatedFriends.push({
                id: friend.id,
                image: friend.picture,
                text: `${friend.first_name} ${friend.last_name}`,
                icon: mdiMinusCircle,
                hidden: false
            });
        });
    },
    computed: {
        displayedAssociatedFriends: function() {
            return this.associatedFriends.filter(friend => friend.hidden === false)
        }
    },
    props: ['user'],
    data: () => ({
        selectedFriends: [],
        associatedFriends: [],
        iconUser: mdiAccount,
        iconPlusCircle: mdiPlusCircle,
        iconPlus: mdiPlus,
        iconClose: mdiClose,
        errorFriendLookup: null,
        friendEmail: null,
        dialog: false,
        userIDs: ''
    })
}