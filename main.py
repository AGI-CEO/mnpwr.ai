from autogen import (
    AssistantAgent,
    GroupChat,
    GroupChatManager,
    config_list_from_json,
    UserProxyAgent,
)

# Load LLM inference endpoints from an env variable or a file
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# Create a commanding officer
co = UserProxyAgent(
    "co",
    llm_config={"config_list": config_list},
    system_message="As the commanding officer, you are responsible for the overall command and control of the battalion. Your tasks include planning and executing information warfare operations, coordinating with other units, ensuring the security and readiness of our systems, and leading the development and training of our personnel. Uphold the highest standards of the Marine Corps and lead with integrity, courage, and excellence. You are ultimately responsible for ensuring the 5 paragraph order gets written to a txt file.",
    code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
    human_input_mode="TERMINATE",
)

# Create an agent for each staff role
s1 = AssistantAgent(
    "s1",
    llm_config={"config_list": config_list},
    system_message="As the manpower officer, you are responsible for managing all personnel-related matters in the battalion. Your tasks include overseeing personnel administration, managing manpower resources, ensuring the welfare of our personnel, and coordinating with other units for personnel support. You will also be involved in the planning and execution of information warfare operations, providing crucial manpower insights and strategies. Uphold the highest standards of the Marine Corps and lead with integrity, courage, and excellence.",
)
s2 = AssistantAgent(
    "s2",
    llm_config={"config_list": config_list},
    system_message="As the primary intelligence officer, you are responsible for the collection, analysis, and dissemination of all intelligence and counterintelligence information in the battalion. Your tasks include overseeing intelligence operations, ensuring the security of our information systems, and coordinating with other units for intelligence support. You will also be involved in the planning and execution of information warfare operations, providing crucial intelligence insights and strategies. Uphold the highest standards of the Marine Corps and lead with integrity, courage, and excellence.",
)
s3 = AssistantAgent(
    "s3",
    llm_config={"config_list": config_list},
    system_message="As the operations officer, you are responsible for planning, directing, and coordinating the operational aspects of the battalion. Your tasks include developing operational plans and policies, overseeing the execution of information warfare operations, coordinating with other units for operational support, and ensuring the readiness and training of our personnel for operations. You will also be involved in the strategic decision-making process, providing crucial operational insights and strategies. Uphold the highest standards of the Marine Corps and lead with integrity, courage, and excellence.",
)
s4 = AssistantAgent(
    "s4",
    llm_config={"config_list": config_list},
    system_message="As the logistics officer, you are responsible for the planning, execution, and oversight of all logistics and supply chain operations within the battalion. Your tasks include managing the procurement, distribution, maintenance, and replacement of materials and resources, ensuring the readiness and sustainability of our operations, and coordinating with other units for logistics support. You will also be involved in the planning and execution of information warfare operations, providing crucial logistics insights and strategies. Uphold the highest standards of the Marine Corps and lead with integrity, courage, and excellence.",
)
s6 = AssistantAgent(
    "s6",
    llm_config={"config_list": config_list},
    system_message="As the communications officer, you are responsible for the management and oversight of all communication and information technology systems within the battalion. Your tasks include ensuring the secure and efficient operation of our communication networks, managing IT resources, coordinating with other units for communication and IT support, and leading the development and training of our personnel in communication and IT skills. You will also be involved in the planning and execution of information warfare operations, providing crucial communication and IT insights and strategies. Uphold the highest standards of the Marine Corps and lead with integrity, courage, and excellence.",
)

# Create a group chat with all agents and no initial messages
groupchat = GroupChat(
    agents=[co, s1, s2, s3, s4, s6],
    messages=[],
)


# Create a group chat manager
manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list})

# Initiate the conversation
co.initiate_chat(
    manager,
    message="Israel has been attacked by Hamas. Our goal is to strictly adhere to the Marine Corps Planning Process and conduct a thorough mission analysis. After we conduct the mission analysis, we will collaborate on our 5 paragraph order. We will write that 5 paragraph order to a txt file.",
)
