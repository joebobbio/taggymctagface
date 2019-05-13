const {
    Command
} = require('discord.js-commando');
const {
    MessageEmbed
} = require('discord.js');
const SQLite = require("better-sqlite3");
const sql = SQLite('./commands.sqlite');

module.exports = class HelpCommand extends Command {
    constructor(client) {
        super(client, {
            name: 'help',
            group: 'custom commands',
            memberName: 'help',
            description: 'List bot commands',
            guildOnly: true,
            userPermissions: ['MANAGE_MESSAGES'],
            examples: ['help']
        });
    }

    run(msg) {
        const embed = new MessageEmbed()
        .setTitle("Taggy McTagface's Command List")
        .addField("$add", "Add a new custom command to the database. Commands can optionally have arguments, which are appended to the end of whatever the response is.\n**Paramenters**:\n - `<command>`: the name you want for the command\n -`<args>` true/false, depending on if you want args or not.\n - `<response>`: The output you want when a user invokes the command.\n**Example usage**: $add camsucks false Cam you really suck\n----------")
        .addField("$delete", "Delete a custom command from the database.\n**Parameters:**\n - `<ID>`: The ID of the command you want to delete. You can find this by using the `$ls` command and looking for the command you want to delete (if you have two versions of the same command i.e with and without args, make sure to choose the correct one!\n**Example usage:** `$delete 12345\n----------")
        .addField("$ls", "List all custom commands belonging to your server.\n----------")
        .addField("How to use a custom command", "You should know the name of the command you want to invoke. Simply use `$<command name here>` and the response will be posted.\n**Example usage**: `$camsucks`")
        .setFooter("Created with ❤️ by SlimShadyIAm#9999. Give me a pat on the back some time!")
        .setColor(7506394);

        msg.channel.send({ embed })
    }
}