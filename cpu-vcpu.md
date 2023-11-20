- CPU (Central Processing Unit):
  - Physical Hardware: The CPU is the physical hardware component of a computer that performs the actual processing of instructions. It executes instructions from programs, performs calculations, and manages data.

- vCPU (Virtual CPU):
  - Virtualized Instance: In a virtualized environment (such as virtual machines), a vCPU is a virtualized or emulated representation of a physical CPU core. It's a portion of the physical CPU resources allocated to a virtual machine.
  Abstraction Layer: The hypervisor (virtualization layer) creates and manages vCPUs. Each vCPU represents a share of the physical CPU's processing power.

- Relationship:

  - A vCPU is a virtual abstraction of a physical CPU core. Multiple vCPUs can be created and assigned to different virtual machines running on the same physical server.
- Key Points:

  - Allocation: The number of vCPUs assigned to a virtual machine determines the virtual machine's processing capacity. For example, a virtual machine with 2 vCPUs has access to the processing power of two physical CPU cores.


- Example:

  - If you have a physical server with a quad-core CPU (4 cores) and you create three virtual machines, each configured with 2 vCPUs, you are overcommitting the CPU resources. The hypervisor manages the allocation of physical CPU time to each vCPU based on demand.

- Note:

  - While vCPUs provide flexibility and resource isolation in virtualized environments, it's important to consider the physical CPU capabilities and avoid overcommitting resources to prevent performance degradation. The performance of virtual machines depends on the available physical CPU resources and the efficiency of the hypervisor's scheduling algorithms. You can run into performance and capacity issue

- Why virtualization?
- Complexities introduced by Virtualization: 
  - Over-committment can become a problem if performance monitoring is not done.
  - Blended storage IO: "The IO Blender Effect". Underlying memory users are all vying for the same storage, with each having distinct requirements, which can make it a challenge to properly allocate.
  - Troubleshooting becomes more complex.

- The Fundamentals of Server Virtualization:
- Benefits
  -  Efficiency:
    - Scaling by creating new VMs from templates.
    - Scaling by cloning VMs
    - Adding more resources on demand.
    - Admininstering many VMs from a single console.
    - Preserving state of a VM by snapshotting.
    - Policy-driven management.
  - Agility:
    - Rapid deployment of new applications.
    - Rapid scaling of new applications.
    - Break down admininstrative silos in IT and reallocate time to business-impacting projects.
  - Availability:
    - Abstraction. What is virtualized in software becomes relatively independent of underlying hardware, and therefore, portable.
    - High availability for all. Availability that was once very difficult and expensive becomes standard. This high availability is takes the form of fast replacement of suddenly unavailable resources, among other ways.
    - Improved data protection and disaster recovery through offsite redundancy.
    - Reduced energy consumption through efficiency of resource use during runtime and powering down during hours where they are not needed.
    - Increased business agility. Faster scaling. 
  - Time savings:
    - Admininstering servers.
    - Protecting data.
    - Deploying new applications.
    - Replacing aging harwire.
    - Enabling HA and Loadbalancing.
  - Money:
    - Fewer servers = lower associated infrastructure costs.
    - More efficient administration of IT. Reallocation of labor.
  - Job security:
    - Deploy new apps faster.
    - Make server refresh easy
    - Spend more time on business-impacting projects.
  - Performance optimization. Hot-add / hot-plug. Resouces can be scaled up as needed (in some cases, without downtime)
  - Load balancing. Built-in load balancing ensures all applications get the resources they need, when they need them.
  - Resource sharing. Physical resources are shared and consumption is optimized.
- Server Virtualization Architecture
  - Hypervisor: the software that runs virtual machines. 
  - The server virtualization layer resides between the physical server and the virtualized servers.
  - Type 1 Hypervisor
    - Loaded directly on the hardware. Replaces the OS.
      - Examples: Hyper-V, ESXi / VSphere, KVM
  - Type 2 Hypervisor
    - Loaded in an OS running on the hardware.
      - Examples: Workstation / Fusion, Oracle VBox, Parallels
    - Requires and extra layer and therefore extra resources.
  - Virtual Host: The physical hosts that are running the hypervisor.
  - VMs and Virtual Resources:
  - Storage Virtualization
    - Virtual disk: These are actually just files, that represent entire virtual hard drives that can be moved.
  - Centralized management.
  - Management APIs.


  - Overcommittment of resources:
    - This happens when the VMs are allocated more resources than the physical has to give. You can run into performance and capacity issues, but the hypervisor is actually very efficient and smart about optimizing resources, especially memory. In the case of memory, it will share memory, compress memory, and in the worst case, use a swap file. Overcommittment is used commonly in data centers and 9 times out of 10, there is no trouble, as long as you properly monitor performance.
  - Overcommitment: Hypervisors often allow overcommitment, where the total vCPUs allocated to virtual machines can exceed the actual number of physical CPU cores. This is possible because not all virtual machines may use their allocated CPU resources simultaneously.
    
  - The VMs are hardware indenpendent.
  - Network Virtualization
    - Virtual Switches
    - Virtual Firewalls
    - Virtual NICs
      - These map back to physical network adapters.
  - Virtual Desktop
  - IO
    - Virtual ethernet, fiber, hardware connections (IO pathways)
  - Application
    - The application and all necessary dependencies.

